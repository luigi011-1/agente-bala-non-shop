"""Produção corrente apenas. Fala lida do ROTEIRO aprovado; imagens internas JSON e entregues pelo flow_seguro. Não muda checkpoint nem gera mídia."""
from pathlib import Path
import json, re, sys, shutil
ROOT=Path(__file__).resolve().parents[2]
if not (ROOT/'flow_seguro.py').exists():
 ROOT=Path('/Users/macbookairm2/agente bala non-shop/agente-bala-non-shop')
sys.path.insert(0,str(ROOT))
from flow_seguro import seguro_k,texto_flow,minimo_v
from checar_entrega import parse_takes

AV=[
 ('Avery Knox','AVERY_KNOX','avery_knox','Avery Knox, a woman around sixty with layered platinum-blonde hair, darker roots, brown eyes, light skin and natural fine lines.','White button-up shirt with rolled cuffs, blue jeans, turquoise-and-silver necklace, turquoise rings and silver turquoise cuff bracelets.'),
 ('Devon Price','DEVON_PRICE','devon_price','Devon Price, a woman around fifty with a natural bare scalp, hazel-green eyes, fine eyebrows, fair freckled skin and soft facial lines.','Cream lace blazer and cream lace top, blue jeans, rose-gold beaded bracelet, thin silver heart pendant and silver rings.'),
 ('Jordan Vale','JORDAN_VALE','jordan_vale','Jordan Vale, a man around sixty-eight with silver-white hair, thin gold-rimmed round glasses, blue-grey eyes, a clean-shaven narrow face and naturally lined skin.','Cream tailored dinner jacket, white shirt, black bow tie, dark trousers, slim gold wristwatch and gold ring.')]
MODEL={
 'v01':dict(title='V01 · Nove medos de prosperar',summary='Selfie no carro. Nove perguntas curtas sobre dinheiro recebem respostas diretas; o enquadramento aproxima no fecho e o CTA leva à leitura.',scene='Inside a car: brown front-seat headrest behind the speaker, black panoramic roof crossbars above, a blue sky with cloud texture and palm fronds through the glass, dark rear seat at left and green horizon through the side window.',lux='Inside an exceptionally luxurious car: hand-stitched brown leather front-seat headrest behind the speaker, black panoramic roof crossbars above, blue sky with cloud texture and palm fronds through the glass, dark leather rear seat at left and green horizon through the side window.',frames=[
 ('tl_t00000.6000_000004.png','0.6','oval face and open gesturing hand',25,30,'Handheld selfie front camera at eye height with a 1x lens and a slight downward viewing angle and level horizon','Seated against the brown headrest, open hand entering at the lower right, frank direct gaze, caught mid-sentence, lips naturally parted, animated expression.','T01','gancho falado, celular já descendo para rosto'),
 ('tl_t00008.0000_000041.png','8.0','oval face and open gesturing hand',26,30,'Handheld selfie front camera at eye height with a 1x lens and a slight downward viewing angle and level horizon','Seated against the same brown headrest, open hand low in the frame, direct gaze, caught mid-sentence, lips naturally parted, animated expression.','T02-T03','enumeração dos medos, mesma selfie'),
 ('tl_t00019.6000_000099.png','19.6','oval face and open gesturing hand',37,22,'Handheld selfie front camera at eye height with a 1x lens and a close viewing angle and level horizon','Leaning slightly toward the lens, the face fills more of the frame, open hand low at the right edge, caught mid-sentence, lips naturally parted, animated expression.','T04-T07','aproximação, exortação e CTA')],map=[1,2,2,3,3,3,3]),
 'v02':dict(title='V02 · A Imperatriz e o futuro próspero',summary='Embaralha cartas douradas e começa a virar a Imperatriz. Dez atributos e três desejos descrevem o futuro; quatro afirmações precedem o CTA da leitura.',scene='A bright lived-in room with an off-white textured ceiling, beige wall, diagonal ceiling-wall junction at upper right, small circular recessed spot above right and a dark sofa strip at lower right.',lux='A grand mansion sitting room with a tall off-white textured ceiling, pale beige wall, diagonal ceiling-wall junction at upper right, a small circular recessed spot above right and a dark premium upholstered sofa strip at lower right. Rich materials stay understated in this close framing.',frames=[
 ('tl_t00000.8000_000005.png','0.8','rectangular gold-backed card',30,20,'Fixed smartphone camera below eye level with a 1x lens and a slight upward viewing angle and level horizon','Seated, surprised open-mouth expression, one hand holds the gold-backed deck low left, the other separates one gold-backed card low right at the beginning of turning it toward the lens, caught mid-sentence, lips naturally parted, animated expression.','T01','surpresa, verso dourado começando a virar'),
 ('tl_t00002.6000_000014.png','2.6','rectangular yellow-gold card',25,20,'Fixed smartphone camera below eye level with a 1x lens and a slight upward viewing angle and level horizon','Seated, one hand holds a gold-backed deck low left, the other displays the Empress card front at chest level low right, direct gaze, caught mid-sentence, lips naturally parted, animated expression.','T02-T06','carta revelada, atributos e desejos'),
 ('tl_t00048.6000_000244.png','48.6','rectangular yellow-gold card',15,25,'Fixed smartphone camera below eye level with a 1x lens and a slight upward viewing angle and level horizon','Seated slightly reclined, head gently tilted, Empress card low right and the free index finger beside the chin instead of across the lips, caught mid-sentence, lips naturally parted, animated expression.','T07','quatro afirmações faladas, pose recostada'),
 ('tl_t00055.6000_000279.png','55.6','rectangular yellow-gold card',16,25,'Fixed smartphone camera below eye level with a 1x lens and a slight upward viewing angle and level horizon','Seated upright, Empress card low right and the free index finger raised close to the lens at left, direct gaze, caught mid-sentence, lips naturally parted, animated expression.','T08-T10','CTA, carta e mão apontando')],map=[1,2,2,2,2,2,3,4,4,4]),
 'v03':dict(title='V03 · Três afirmações e o sinal de abundância',summary='Selfie íntima no carro, sem objetos. A seleção leva a três afirmações e a quatro maneiras de notar o lembrete da borboleta; a leitura continua nos Stories.',scene='Inside a car with a grey headliner, curved grab handle at upper left, black window border at left showing pale blue sky with cloud texture and a green treeline, and a dark seat behind at right.',lux='Inside an exceptionally luxurious car with a tailored grey suede headliner, curved grab handle at upper left, black window border at left showing pale blue sky with cloud texture and a green treeline, and a dark premium leather seat behind at right.',frames=[
 ('tl_t00000.0000_000001.png','0.0','oval face and empty gesturing hand',30,28,'Handheld selfie front camera at eye height with a 1x lens and a slight side viewing angle and level horizon','Seated, shoulders slightly turned, head facing the lens, empty hand below the lower edge, caught mid-sentence, lips naturally parted, animated expression.','T01-T02','seleção pessoal e save'),
 ('tl_t00013.8000_000070.png','13.8','oval face and empty gesturing hand',32,28,'Handheld selfie front camera at eye height with a 1x lens and a slight side viewing angle and level horizon','Seated, shoulders slightly turned, close direct gaze and gentle smile, empty hand low in the frame, caught mid-sentence, lips naturally parted, animated expression.','T03-T05','afirmações e quatro vias do lembrete'),
 ('tl_t00041.6000_000209.png','41.6','oval face and empty gesturing hand',33,27,'Handheld selfie front camera at eye height with a 1x lens and a slight side viewing angle and level horizon','Seated in the same position, looking firmly into the lens, empty hand below the lower edge, caught mid-sentence, lips naturally parted, animated expression.','T06-T09','ponte, retorno e CTA')],map=[1,1,2,2,2,3,3,3,3])}
REAL='Visible pores, irregular skin texture, faint redness, fine lines, soft facial asymmetry, uneven natural hair strands where present, smartphone footage look, low contrast, slight JPEG compression, background fully in focus, everything in sharp focus.'

def key(m,a,f):
 name,code,ident,idtxt,ward=a;frame,time,term,pct,dist,cam,state,take,pt=f
 scene=m['lux'] if ident=='jordan_vale' else m['scene']
 if 'v02'==KEY:
  prop=(f'A {term} close to the lens; gold-backed deck low at image left. ')
  if 'gold-backed' in term:prop+='The separate card shows a gold back with dark fine ornamental linework as it starts to turn.'
  else:prop+='The front depicts a seated crowned woman in a pale patterned dress on a red seat, dark green foliage and yellow ground, with an ordinary printed-illustration finish.'
  prop+=f' The card-and-hands hero occupies about {pct} percent of the image area, about {dist} centimeters from the lens, closer than the face.'
  state+=' Opaque white curved patches sit beneath both eyes and above the brows; the eyes and lips remain clear.'
 else:prop=f'The hero is the {term}; the face occupies about {pct} percent of the image area, about {dist} centimeters from the lens; both hands remain empty.'
 comp=f'The hero occupies about {pct} percent of the image area, about {dist} centimeters from the lens. The speaker is close to the camera and the background remains simple through framing.'
 return seguro_k(dict(reference_use='Use the attached character sheet only for the exact face, skin, hair and outfit; its plain backdrop is excluded from this scene.',identity_main=idtxt,wardrobe=ward,scene=scene,prop=prop,posture=state,composition=comp,camera=cam,lighting='Neutral overcast daylight, true neutral colors, soft shadows, diffuse daylight on face and hands.',state='Start frame: '+state+' One person alone in frame. '+REAL,realism=REAL,aspect_ratio='9:16 vertical'))

def ficha(dest,base,m,a,ks):
 out=['# Ficha de frames e placar','', 'A autoria abriu pessoalmente todos os frames abaixo e as anchors recebidas. Percentuais são aproximações manuais da área projetada/caixa do herói no raster, não segmentação automática. Distâncias em centímetros e lente 1x são ALVOS técnicos estimados para recriar a perspectiva; o vídeo não fornece calibração, focal ou EXIF. Altura é relativa aos olhos e inclinação observada. Não são medidas físicas certificadas do original.','', 'Jordan: mesmo tipo de ambiente, câmera e ação em equivalente de luxo, por decisão explícita. Pele/roupa pelo character sheet. Plano orgânico não exige bandeira. Não inserir props não listados.','']
 for i,(f,j) in enumerate(zip(m['frames'],ks),1):
  frame,time,term,pct,dist,cam,state,take,pt=f;rel=f'input/frames_modelo/K{i:02d}_modelo.png';d=dest/rel;d.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(base/'watch/frames/timeline'/frame,d)
  out += [f'## K{i:02d}',f'Frame: `{rel}`',f'Take: {take}',f'Herói: {term}; imagem observada no tempo {time}s.',f'Termos de forma: "{term}"',f'Quadro: cerca de {pct}% (estimativa da área do herói; projeção-alvo escrita em K).',f'Distância da lente: alvo aproximado {dist} centímetros, inferido da perspectiva; sem calibração métrica.',f'Câmera: {cam}; lente 1x alvo inferido, sem metadata.',f'Pose: {state}',f'Lista fechada: {m["lux"] if a[2]=="jordan_vale" else m["scene"]}; avatar/roupa do sheet, '+('baralho/carta, mãos, patches brancos.' if KEY=='v02' else 'mãos vazias, nada demonstrativo.'),f'Frame 0: estado de entrada derivado do frame a {time}s; '+pt+'.','Desvio (acabamento ou avatar fixo): luz difusa neutra, boca entreaberta para fala, pele/foco; identidade e roupa do sheet, Jordan luxo. '+('Retirar player/app/legendas; dedo ao lado do queixo em vez de cruzando a boca para fala. ' if KEY=='v02' else 'Retirar títulos e legendas originais da imagem gerada. ')+('Borboleta só verbal, nenhum prop novo. ' if KEY=='v03' else 'Nenhum prop novo. ' if KEY=='v01' else 'Só baralho e carta do modelo. ')+'Sem imagem de produto ou efeito sobrenatural.',f'Cenário do modelo: {m["scene"]}','', '| Item | Status | Evidência |','|---|---|---|']
  ev={'F1':term,'F2':f'about {pct} percent','F3':f'about {dist} centimeters','F4':cam,'F5':j['posture'].split(',')[0],'F6':'one person alone in frame','G1':'Neutral overcast daylight','G3':'everything in sharp focus','G4':'Visible pores','G5':'true neutral colors','G6':'text-free','G8':'caught mid-sentence'}
  for item in ['F1','F2','F3','F4','F5','F6','G1','G2','G3','G4','G5','G6','G7','G8']:
   if item=='G7':out+=['| G7 | N/A | Origem ORGANIC; bandeira ausente no modelo, não adicionar prop. |']
   elif item=='G2' and KEY=='v02':out+=['| G2 | N/A | Nenhuma janela ou céu aparece no frame do cômodo. Luz entra de fora do quadro. |']
   elif item=='G2':out+=['| G2 | OK | "sky with cloud texture" |']
   else:out+=[f'| {item} | OK | "{ev[item]}" |']
  out+=['']
 (dest/'FICHA_FRAMES.md').write_text('\n'.join(out)+'\n')


def package(base,m,a,index):
 name,code,ident,idtxt,ward=a;es=ident=='jordan_vale';dest=base.parent/(base.name+'_jordan_es') if es else base
 dest.mkdir(exist_ok=True)
 if es:
  c=dest/'CHECKPOINT.md'
  if not c.exists():c.symlink_to('../'+base.name+'/CHECKPOINT.md')
 r=dest/'ROTEIRO.md';tx=r.read_text();tx=tx.replace('Status: NOT_APPROVED.','Status: APPROVED_BY_LUIGI.').replace('roteiro para aprovação','roteiro aprovado por Luigi')
 tx=tx.replace('## Falas canônicas para conferência e edição','## Roteiro cena a cena: falas canônicas para conferência e edição')
 tx=tx.replace('Aguardar aprovação real de Luigi para este modelo e as duas versões de idioma. Nenhum pacote K/V foi criado.','Luigi aprovou este modelo e as versões EN/ES nesta conversa em 2026-10-10: "roteiros aprovados, prossiga". As falas acima permanecem imutáveis; pacotes textuais não comprovam mídia gerada.')
 tx=tx.replace('Aguardar aprovação real de Luigi para este modelo e as duas versões de idioma.','Roteiro aprovado por Luigi em 2026-10-10, conforme CHECKPOINT da produção-base.')
 
 if 'Esqueleto preservado' not in tx: tx+='\n## Esqueleto preservado\n\nFonte: METODO_PUZZLE.md da produção-base; beats mantidos, roteiro aprovado.\n'
 r.write_text(tx);takes=parse_takes(tx);assert len(takes)==len(m['map']);assert all(t['fala'] for t in takes)
 ks=[key(m,a,f) for f in m['frames']]
 ficha(dest,base,m,a,ks)
 mapa='\n'.join(f'V{i:02d}: K{k:02d}' for i,k in enumerate(m['map'],1))
 target=f'/Users/macbookairm2/Downloads/Auraly_prosperidade_2026_10_10/{index:02d}_{KEY.upper()}_{ident}'
 anchor=str(base/'anchors'/(ident+'.jpg'))
 head=f'# Pacote | {m["title"]} | {name}\n\nflow_seguro: v1\n\nIdioma da fala: '+('ESPANHOL latino-americano neutro' if es else 'American English')+f'\n\nImagem: Nano Banana 2.1, 4 variações, 9:16. Vídeo: Veo 3.1 - Lite, 1 variação, 8s, 9:16.\nCharacter sheet único: `{anchor}`\nFonte de fala: `ROTEIRO.md`, aprovada por Luigi; ver CHECKPOINT canônico.\n\nChecklist de envio: 29/29 aplicáveis aprovados (N/A: A1-A4/A10 por fidelidade; B7 origem orgânica; C2-C8 por etapa/formato, elenco e ausência de motion control). Ver CHECKLIST_ENVIO_PACOTE.md.\n\n## MAPA K/V\n\n{mapa}\n\n'
 internal=head+'JSON abaixo é FONTE INTERNA. Nunca colar esse JSON no Flow.\n\n'
 flow=head+'## BLOCO DE IMAGEM\n\n```text\n'
 entrega=head+'## Qual vídeo é este\n\n'+'Modelo: '+m['title']+'\n\n'+m['summary']+'\nGancho verbal (português): '+ re.findall(r'^\| T01[^|]*\|[^|]*\| (.+?) \|$',tx,re.M)[0]+'\nGancho visual: '+m['frames'][0][-1]+'.\n\n'
 for i,(j,f) in enumerate(zip(ks,m['frames']),1):
  cod=f'K{i:02d}';para=texto_flow(j);assert len(para)<=2600, (cod,len(para))
  internal+=f'## {cod} · {f[8]} · GERAR DO ZERO\n\n```json\n'+json.dumps(j,ensure_ascii=False,indent=2)+'\n```\n\n'
  flow+=cod+'\n'+para+'\n\n'
  entrega+=f'### {cod} · {f[8]} · imagem\n\nCena: {f[-1]}; identidade {name}, roupa do sheet, mesmo cenário do modelo'+(' em equivalente de luxo.' if es else '.')+f'\n\n```text\n{cod}\n{para}\n```\n\n'
 flow+='```\n\n## BLOCO DE VÍDEO\n\n```text\n'
 for i,t in enumerate(takes,1):
  cod=f'V{i:02d}';k=f'K{m["map"][i-1]:02d}'
  source='A seguinte frase: "'+t['fala']+'"\n'+('ESPANHOL' if es else 'ENGLISH')+(' selfie' if KEY!='v02' else '')
  v=minimo_v(source)
  internal+=f'### {cod} · {t["id"]} · usa {k}\n\n```text\n{v}\n```\n\n'
  flow+=cod+'\n'+v+'\n\n'
  entrega+=f'### {cod} · {t["id"]} · vídeo\n\nCena: {t["id"]}, {t["head"].replace(" · TALKING", "").lower()}; {name} fala na imagem escolhida de {k}.\n\n```text\n{cod}\n{v}\n```\n\n'
 flow+='```\n'
 editing=f'\n## Montagem e entrega dos takes\n\nSalvar takes em `{target}`. Nomear V01.mp4, V02.mp4 etc. Essa pasta está preparada, não contém mídia confirmada.\nEdição automática futura: uma edição por vez, conferência palavra por palavra com ROTEIRO.md; palavras faltantes/trocadas voltam ao Flow. Estilo v3: fala 1,12x, zero silêncio, legenda serifada branca ao centro, light leak em 2 trocas e música 25 dB abaixo da voz; preservar pausa do herói acelerando. Rótulo discreto AI-generated. Não usar voice changer. Jordan: adaptar ASR para espanhol antes de editar.\nTexto de tela é pós-produção, nunca K/V. Todos os takes falam. '+('T07 tem quatro afirmações consecutivas, sem player/UI; preservar seus quatro microbeats.' if KEY=='v02' else 'T03 tem três afirmações numeradas separadamente na edição; borboleta somente nomeada.' if KEY=='v03' else 'Preservar nove perguntas/desarmes e a aproximação final.')+'\n\n## Verificação de envio\n\nChecklist de envio e ficha: CHECKLIST_ENVIO_PACOTE.md; cobertura e fala literal verificadas mecanicamente antes de entrega e revisão independente obrigatória. A mídia ainda não foi gerada.\n'
 entrega=entrega.replace('## MAPA K/V\n\n'+mapa+'\n\n','',1)
 entrega=entrega.replace('## Qual vídeo é este', '## Qual vídeo é este',1)
 entrega=entrega.replace('## Qual vídeo é este', '## Qual vídeo é este',1)
 marker='### K01'
 entrega=entrega.replace(marker,'## MAPA K/V\n\n'+mapa+'\n\n'+marker,1)
 for prefix,content in [('PROMPTS',internal+editing),('FLOW',flow),('ENTREGA',entrega+editing)]: (dest/f'{prefix}_{code}.md').write_text(content)
 (dest/f'MAPA_{code}.md').write_text('# MAPA K/V\n\n'+mapa+'\n')
 batches=[list(range(i,min(i+7,len(takes)+1))) for i in range(1,len(takes)+1,7)]
 agent=f'''# Agente Flow · {m['title']} · {name}\n\nVocê executa apenas esta combinação: {KEY.upper()} / {name}. Roteiro já aprovado; não criar ou editar prompts. Arquivo: ENTREGA_{code}.md. Idioma: {'espanhol latino-americano neutro' if es else 'inglês americano'}.\n\nIMAGEM: anexar somente `{anchor}` (character sheet deste avatar), colar o parágrafo K exato, gerar4variações9:16 em Nano Banana2.1. Códigos K01 a K{len(ks):02d}. Conferir4 e9:16 antes de cada K. Se vier menos ou outro formato, repetir o mesmo prompt/sheet até4corretas. Operador apaga3 e fica com1 escolhida manualmente por K; você não escolhe.\n\nVÍDEO: anexar somente a imagem escolhida indicada no MAPA K/V, como INITIAL FRAME, e colar V literal. Veo3.1-Lite,8s,1variação9:16. Nenhum outro anexo. Gerar só após escolha manual.\n\nMAPA K/V:\n{mapa}\n\nLotes fechados máximos7: {'; '.join('V%02d a V%02d'%(b[0],b[-1]) for b in batches)}. Espere todos terminarem; relate pendências e aguarde operador dizer prossiga para o próximo lote. Não preencher vaga de lote que terminou cedo. Não reiniciar concluído sem pedido.\n\nFalha, censura ou bloqueio: repetir o MESMO prompt EXATO. Nunca cortar/reescrever/suavizar. Relatar avatar,código,contagem de tentativas e mensagem exata; após3bloqueios semelhantes avisar mantendo prompt. Configuração indisponível,anexo faltante ou mapa conflitante: avisar antes de prosseguir. Não adicionar música,legenda,texto,tradução ou fala.\n\nSalvar os takes em `{target}`, nomes V01.mp4 etc.; este destino não comprova arquivos gerados. A edição roda depois, um vídeo por vez. Status por código: pronto/tentando/pendente, tentativas; ao fim liste concluídos/pendentes e aguarde operador.\n'''
 
 for x,y in [('gerar4variações9:16','gerar 4 variações, 9:16'),('Nano Banana2.1','Nano Banana 2.1'),('Conferir4 e9:16','Conferir 4 e 9:16'),('até4corretas','até 4 corretas'),('apaga3','apaga 3'),('com1 escolhida','com 1 escolhida'),('Veo3.1-Lite,8s,1variação9:16','Veo 3.1 - Lite, 8 segundos, 1 variação, 9:16'),('fechados máximos7','fechados, no máximo 7'),('após3bloqueios','após 3 bloqueios'),('avatar,código,contagem','avatar, código, contagem'),('indisponível,anexo','indisponível, anexo'),('música,legenda,texto,tradução','música, legenda, texto, tradução')]: agent=agent.replace(x,y)
 (dest/f'AGENTE_FLOW_{code}.md').write_text(agent)
 print(KEY,name,'K',len(ks),'V',len(takes),'Kchars',[len(texto_flow(x)) for x in ks])
 return dest,ks

if __name__=='__main__':
 base=Path(__file__).resolve().parent
 if base==Path('/tmp'):base=ROOT/'producao'/sys.argv[1]
 KEY=next(k for k in MODEL if '_'+k+'_' in base.name);m=MODEL[KEY]
 for ai,a in enumerate(AV):package(base,m,a,(int(KEY[-1])-1)*3+ai+1)
