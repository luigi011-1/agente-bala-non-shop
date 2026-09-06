import json
import math
import subprocess
import sys
from pathlib import Path

from . import provider as ai, storage as store
from .rules import ROOT, validate_analysis, validate_imageset, validate_script


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def extract(pid):
    folder = store.folder(pid)
    manifest = folder / 'watch/manifest.json'
    if manifest.exists():
        store.event(pid, 'Extração anterior encontrada; retomando sem repetir o processamento.')
    else:
        store.event(pid, 'Executando /watch: cenas, timeline 5 fps e transcrição Whisper local.')
        command = [sys.executable, '-u', str(ROOT / '.claude/skills/watch/scripts/watch_pipeline.py'),
                   '--video', str(folder / 'source.mp4'), '--outdir', str(folder / 'watch')]
        with (folder / 'watch.log').open('w', encoding='utf-8') as log:
            result = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT,
                                    cwd=ROOT, timeout=2400)
        if result.returncode or not manifest.exists():
            raise ValueError('A extração falhou. Consulte watch.log nos arquivos do projeto.')
    m = read(manifest)
    expected = math.floor(m['info']['duration'] * 5)
    if len(m['timeline']) < max(1, expected - 1):
        raise ValueError('Timeline incompleta. Não é seguro seguir com uma análise parcial.')
    transcript_path = folder / 'watch/audio/transcript.json'
    if not m.get('transcript') or not transcript_path.is_file():
        raise ValueError('Não há transcrição completa. Verifique áudio e instalação do Whisper.')
    transcript = read(transcript_path)
    if not isinstance(transcript, list) or not transcript or not any(s.get('text', '').strip() for s in transcript):
        raise ValueError('A transcrição está vazia. Confira o áudio antes de continuar.')
    store.change(pid, extraction=m, status='extracted')
    store.event(pid, f"Extração concluída: {len(m['timeline'])} frames. Análise visual ainda pendente.")


def analyze(pid):
    ai.require_think_key()
    folder, p = store.folder(pid), store.get(pid)
    m = p['extraction']
    transcript = read(folder / 'watch/audio/transcript.json')
    notes = []
    sheets = m['overview']['scenes'] + m['overview']['timeline']
    cache = folder / 'analysis_cache'
    cache.mkdir(exist_ok=True)
    for i, sheet in enumerate(sheets):
        store.event(pid, f'/watch visual: grade {i + 1}/{len(sheets)}. Todos os frames serão percorridos.')
        checkpoint = cache / (sheet + '.json')
        if checkpoint.exists():
            note = read(checkpoint)
        else:
            note = ai.think(pid,
                'Inspect every timestamped frame in this sheet in temporal order. Return JSON '
                '{observations:[{start:number,end:number,visual:string,people:number,props:string,'
                'action:string,reveal:string}], peak_times:[number], uncertain:[string]}. '
                'Give Portuguese descriptions. Flag subtle physical changes and exact peak times '
                'for full-resolution follow-up; never infer action only from dialogue.',
                {'transcript': transcript, 'sheet': sheet}, [folder / 'watch/overview' / sheet])
            store.write_json(checkpoint, note)
        notes.append(note)
    # Every hook frame, plus before/at/after every nominated event, at original resolution.
    desired = {f['t'] for f in m['timeline'] if f['t'] <= 8}
    for note in notes:
        for t in note.get('peak_times', []):
            if isinstance(t, (int, float)) and 0 <= t <= m['info']['duration']:
                desired.update([max(0, t - .2), t, t + .2])
    files = sorted({min(m['timeline'], key=lambda f: abs(f['t'] - t))['file'] for t in desired})
    details = []
    for start in range(0, len(files), 6):
        chunk = files[start:start + 6]
        store.event(pid, f'/watch: conferindo frames originais {start + 1}–{min(start + 6, len(files))}/{len(files)}.')
        checkpoint = cache / f'full_{start}.json'
        if checkpoint.exists():
            detail = read(checkpoint)
        else:
            detail = ai.think(pid,
                'Inspect these original-resolution temporal frames. Return JSON '
                '{observations:[{time:string,action:string,hero:string,props_owner:string}],'
                'uncertain:[string], confirmed_reveals:[string]}. Do not claim audio was heard.',
                {'transcript': transcript, 'frames': chunk},
                [folder / 'watch/frames/timeline' / f for f in chunk])
            store.write_json(checkpoint, detail)
        details.append(detail)
    store.event(pid, '/watch: consolidando beats, herói e evidências de movimento.')
    analysis = ai.think(pid,
        'Synthesize complete /watch from all visual evidence. Return JSON '
        '{summary:string,hero:string,hero_evidence:[number],reveals:[{time:number,description:string}],'
        'beats:[{start:number,end:number,visual:string,people:number,props:string,speech:string,'
        'label:string,type:string,change:string}], ambiguity:boolean,questions:[string],'
        'continuity:string,source_reuse:string}. If hero/reveal is unresolved, ambiguity=true '
        'and ask a precise question. Speech verbatim from transcript; clearly mark uncertainty. '
        'Check library for prior skeleton reuse. Descriptions in Portuguese.',
        {'transcript': transcript, 'overview': notes, 'full_resolution': details,
         'video_info': m['info'], 'direction': p['direction']}, context=True)
    validate_analysis(analysis, m['info']['duration'])
    store.write_json(folder / 'ANALISE.json', analysis)
    store.change(pid, analysis=analysis, transcript=transcript, status='analysis_ready')
    store.event(pid, '/watch concluído. Confira os beats e aprove a análise para continuar.')


SCRIPT_DOCTRINE = (
    'Execute the produzir script stage only. The script is AVATAR-AGNOSTIC: it is copy '
    'modeled from the reference video to sell the Auraly manifestation app, and the same '
    'takes are later produced for every avatar. Follow the source skeleton and structure. '
    'Return JSON {title:string,continuity:string,notes:string,'
    'skeleton:[{beat:string,original:string,adapted:string}],takes:[{id:"T1",beat:string,'
    'speech:string,translation:string,action:string,setup:"A"}]}. '
    'Sequential T ids, 13-29 words per take, English speech single line without double quotes '
    'or em dash. Portuguese beat/action/translation and notes. T1 alone setup A (the hook), '
    'body takes setup B, CTA takes setup C. continuity is a short Portuguese note: same room, '
    'same wardrobe and props across every take; the avatar identity comes from each avatar '
    'anchor photo supplied later. Respect source number/structure, no filler. Fit approximate '
    'source duration and record any timing tradeoff in notes. Do not assert individualized '
    'guaranteed prediction or fabricate scarcity.\n\n'
    'ANGLE 3 COPY DOCTRINE (mandatory, every rule below overrides generic defaults):\n'
    '1. REGISTER: divine, manifestation, faith, law of attraction. ALWAYS blessing, sign, '
    'universe, intention, agreement, claim, receive. NEVER shield, spell, witch, ritual, '
    'circle of protection, conjure, interference, block. The supernatural here is the SIGN, '
    'the universe answering, the blessing, destiny. Never power to manipulate someone.\n'
    '2. THE PROMISE CHAIN (spine of every video, this exact order): she sent a message to '
    'the universe -> the universe answered -> it wants to reveal her soulmate face -> she '
    'seals the agreement (222, follow, save) -> the face is waiting in her STORIES -> '
    'the link button reveals it. The object of desire is THE FACE, never the app, never a quiz.\n'
    '3. KEYWORD is 222 (two two two), never yes. It is congruent with the mystical register '
    '(repeating numbers 11:11, 444 are signs from the universe).\n'
    '4. LEI DO SELO (LAW OF THE SEAL): every engagement action carries its CONSEQUENCE in '
    'what is already coming for her, never a label. She must want to do it on her own.\n'
    '  - 222 comment = ties the sign to HER NAME. "comment two two two, that is how this '
    'gets tied to your name." Comment is WRITING, so it ties/signs/registers. NEVER "say '
    'out loud" or "claim it out loud" (commenting is writing, not speaking).\n'
    '  - Like and save = STRENGTHENS the blessing. "like it and save it, and the blessing '
    'coming to you gets stronger."\n'
    '  - Follow = KEEPS OPEN what she just sealed. "follow me so this stays open." Follow '
    'without a reason is forbidden.\n'
    '  - Few requests, one line each, group when possible. Long lists read as engagement '
    'farming and kill the effect.\n'
    '5. ORDER IS NON-NEGOTIABLE: 222 FIRST, Stories SECOND. The seal comes before the '
    'destination. If the script is short, merge: "Comment two two two, and tap my profile '
    'picture to watch my stories now."\n'
    '6. STORIES IS THE DESTINATION, DM IS RECOVERY. The video promises the face is in '
    'Stories, never in DM. Never say quiz, test, app, plan, price, one-time, or subscription.\n'
    '7. DECLARED MODE (default): when the copy delivered concrete identity proof (the initial, '
    'a physical trait, timing, the WhatsApp trick, "the person who came into your head the '
    'second I said that"), the CTA DECLARES what is in Stories: "their face is already '
    'sitting in there, and it goes away tonight." CURIOSITY mode is exception, only when '
    'the promise was atmospheric from start to finish.\n'
    '8. STORIES URGENCY IS HONEST: "before they disappear" / "it goes away tonight" is true '
    'by platform rule (24h expiry). Prefer it over any fabricated scarcity.\n'
    '9. NEVER SHOW PRODUCT. No app, no phone screen, no mockup. The promise is the '
    'transformation of her life, not access to a product.\n'
    '10. FACE IS NEVER REVEALED IN THE VIDEO. Any portrait/photo/polaroid in scene must '
    'have the face obscured (out-of-focus print, frosted glass, partial reveal, silhouette).\n'
    '11. After the hook take, the avatar holds the SOULMATE CARD and keeps it until the end.\n'
)


def script(pid):
    p = store.get(pid)
    instruction = SCRIPT_DOCTRINE
    if p.get('copy_note', '').strip():
        instruction += ('\nOPERATOR ADJUSTMENT for this revision (apply it, keep every doctrine '
                        'rule above): ' + p['copy_note'].strip())
    result = ai.think(pid, instruction,
        {'analysis': p['analysis'], 'clarification': p.get('clarification', ''),
         'transcript': p['transcript'], 'direction': p['direction'],
         'previous_script': p.get('script') if p.get('copy_note') else None},
        context=True)
    validate_script(result)
    store.change(pid, script=result, status='script_ready')
    store.write_json(store.folder(pid) / 'ROTEIRO.json', result)
    store.event(pid, 'Roteiro pronto para edição e aprovação. As falas só serão fixadas ao aprovar.')


def hooks(pid):
    p = store.get(pid)
    result = ai.think(pid,
        'Return JSON {hooks:[{id:"H1",title:string,mechanism:string,action:string,prop:string,'
        'congruence:string,screen_text:string,risk:string,validated:boolean,reference:string}]}. '
        'Exactly 8-10 varied visual hook options H1,H2,... in Portuguese except screen_text. '
        'All keep exact approved T1 speech. The hooks are AVATAR-AGNOSTIC: the chosen hooks are '
        'produced for every avatar, so describe them without naming any avatar. Each avatar anchor '
        'photo already shows the scene kit and a holographic SOULMATE card on the table; design '
        'every hook from that baseline. Majority use the SOULMATE card as the TARGET of the action. '
        'Mix sourced and novel mechanisms, label actual evidence and avoid claiming an invented '
        'hook is validated. One shot, the avatar performs the action, fits T1, initial state can be '
        'generated.\n'
        'FORMAT: single flat shot, camera at chest height across the table. The avatar chest-up in '
        'the top half, table in the lower third of the SAME frame. She performs the hook action '
        'with her own hands while speaking. No isolated close-up on the table, no separate B-roll. '
        'The hook lives in T1; from T2 onward she holds the SOULMATE card and those takes are '
        'SHARED (body and CTA), so each new hook costs only one image.\n'
        'REGISTER: divine, manifestation, faith. Props that read as manifestation enter (cards, '
        'crystals, candle, incense, bowl with petals). Props or actions that read as pact do not '
        '(no witch, no spell circle, no dark ritual, no inverted symbols). The test is the '
        'READING, not the object.\n'
        'FACE NEVER REVEALED: any hook involving portrait, photo, polaroid must have the face '
        'obscured as a physical property of the object (out-of-focus print, frosted glass, '
        'partial reveal, silhouette), never as camera blur.\n'
        'Order by congruence with the approved copy. Pure clickbait hooks last, marked as such.',
        {'script': p['script'], 'analysis': p['analysis'], 'direction': p['direction']},
        context=True)
    hs = result.get('hooks', [])
    if not 8 <= len(hs) <= 10 or any(h.get('id') != f'H{i}' for i, h in enumerate(hs, 1)):
        raise ValueError('O modelo não entregou 8–10 ganchos com identificadores válidos.')
    for h in hs:
        if any(not isinstance(h.get(k), str) or not h[k] for k in
               ['title', 'mechanism', 'action', 'prop', 'congruence', 'screen_text', 'risk', 'reference']):
            raise ValueError('Gancho com campos obrigatórios ausentes.')
    store.change(pid, hooks=hs, status='hooks_ready')
    store.event(pid, 'Selecione até 5 ganchos visuais. Eles valem para todos os avatares.')


def imageset(pid):
    """Turn the approved script + selected hooks into one image prompt per hook,
    plus one shared body prompt and one shared CTA prompt. Avatar-agnostic."""
    p = store.get(pid)
    hs = [next(h for h in p['hooks'] if h['id'] == hid) for hid in p['selected']]
    result = ai.think(pid,
        'Create the avatar-agnostic image prompt set. Return JSON {notes:string,frames:['
        '{id:string,title:string,role:"hook|body|cta",hook_id:string|null,takes:[string],'
        'prompt:{scene:string,composition:string,state:string,lighting:string,realism:string,'
        'negative:string}}]}. Use exact role values without the pipe. Produce EXACTLY, in this '
        'order: one frame per selected hook named K01,K02,... in selection order, role "hook", '
        'takes ["T1"], hook_id set to that hook id; then one frame id "BODY" role "body" whose '
        'takes are every setup-B take in script order; then one frame id "CTA" role "cta" whose '
        'takes are every setup-C take in script order. No isolated reference frame, no parent, '
        'no edits. Every prompt is complete English describing a NEW photorealistic vertical 9:16 '
        'image. Do NOT name or describe any avatar: state that the attached anchor photo is the '
        'authority for face, wardrobe and room. The anchor already has a holographic SOULMATE '
        'card on the table: instruct to place that same card model in her hands and keep it from '
        'the hook onward. Keep the seven grouped scene-kit categories (crystals, smoking incense, '
        'white candle, US flag, tarot cards, zodiac artwork, wooden cross). Chest-up framing, '
        'hands and hero in the lower foreground, neutral daylight, real skin, sharp background. '
        'Show the state BEFORE the action, never the completed reveal. Physical SOULMATE title '
        'allowed. negative must include "no captions". Never reveal a real partner face.',
        {'script': p['script'], 'hooks': hs}, context=True)
    validate_imageset(result, p['selected'], p['script'])
    store.change(pid, imageset=result, status='imageset_ready')
    store.event(pid, f'Conjunto de imagens pronto: {len(result["frames"])} por avatar. '
                     'Suba as âncoras dos avatares e prepare a fila do Chrome.')


ACTIONS = {'extract': extract, 'analyze': analyze, 'script': script, 'hooks': hooks,
           'imageset': imageset}
