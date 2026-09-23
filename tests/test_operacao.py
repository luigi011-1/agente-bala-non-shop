import copy
from pathlib import Path
import tempfile
import unittest
from auraly_validacao import (auditar_pacote, objetivo, verificar_estado, sincronizar_fila,
                              validar_portfolio_ganchos)
from gerenciar_operacao import metricas, validar_resultados
import gerenciar_operacao as go
import checar_entrega as ce
import argparse, json
from unittest import mock
from gancho_verbal import validar_camada_verbal

CP = '''Production: exemplo
Angle: ANGLE 3 / Auraly
Objective: SALE
Round: VALIDATION
Reference video: original.mp4
Current stage: PRODUCTION_COMPLETE
Current avatar: NONE
Next action: Wait for new intake.
## Avatar queue
[DONE] Ana
[DONE] Bia
'''
FALA = 'This is the exact approved sentence from the production script.'
VIDEO = 'V01\nVoice: "' + FALA + '" Perfect lip sync. No music.\n'

class Pacotes(unittest.TestCase):
    def auditar(self, video=VIDEO, imagem='K01\nImage prompt.', nome='PROMPTS_VIDEO_ANA.md', takes=None):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); (p/'CHECKPOINT.md').write_text(CP)
            (p/nome).parent.mkdir(parents=True, exist_ok=True)
            (p/nome).write_text(video)
            if imagem is not None:
                (p/nome.replace('VIDEO','IMAGEM')).write_text(imagem)
            return auditar_pacote(p, takes or [{'fala':FALA,'mudo':False}], True)

    def test_limpo_raiz_e_subpasta(self):
        for nome in ('PROMPTS_VIDEO_ANA.md','ana/PROMPTS_VIDEO_FLOW.md'):
            self.assertFalse([x for x in self.auditar(nome=nome) if x[0]=='FALHA'])

    def test_fala_alterada(self):
        self.assertTrue(any(x[1]=='fala-literal' for x in self.auditar(VIDEO.replace('exact','changed'))))

    def test_codigo_duplicado(self):
        self.assertTrue(any(x[1]=='codigos' for x in self.auditar(VIDEO+VIDEO)))

    def test_imagem_ausente(self):
        self.assertTrue(any(x[1]=='casamento-kv' for x in self.auditar(imagem='K02\nImage.')))

    def test_um_k_pode_alimentar_varios_v_com_mapa(self):
        video = VIDEO + VIDEO.replace('V01', 'V02 · K01')
        self.assertFalse([x for x in self.auditar(video=video) if x[0]=='FALHA'])

    def test_v_sem_k_nem_mapa_reprova(self):
        video = VIDEO.replace('V01', 'V02')
        self.assertTrue(any(x[1]=='casamento-kv' for x in self.auditar(video=video, imagem='K01\nImage.')))

    def test_mudo_sem_take_mudo(self):
        self.assertTrue(any(x[1]=='fala-literal' for x in self.auditar('V01\nNo speech. No music.')))

    def test_mudo_aprovado(self):
        self.assertFalse([x for x in self.auditar('V01\nNo speech. No music.', takes=[{'fala':None,'mudo':True}]) if x[0]=='FALHA'])

    def test_checkpoint_obrigatorio_estrito(self):
        self.assertEqual(verificar_estado('',estrito=True)[0][0],'FALHA')
        self.assertEqual(verificar_estado('')[0][0],'AVISO')

    def test_complete_com_pendente(self):
        self.assertTrue(any(x[0]=='FALHA' for x in verificar_estado(CP.replace('[DONE] Bia','[PENDING] Bia'))))

    def test_growth_nao_vem_da_transcricao(self):
        self.assertEqual(objetivo('# Roteiro\n## Modelo\n**Funil:** crescimento'), 'SALE')
        self.assertEqual(objetivo('# Roteiro\n**Funil:** crescimento\n## Modelo'), 'GROWTH')

    def test_sincroniza_por_nome(self):
        fila='| 1 | Bia | anchor-b | PENDING |\n| 2 | Ana | anchor-a | ACTIVE |\n'
        self.assertIn('| 1 | Bia | anchor-b | DONE |',sincronizar_fila(CP,fila))
        with self.assertRaises(ValueError):
            sincronizar_fila(CP,fila.replace('Bia','Carla'))

    def test_sincronizacao_recusa_duplicata(self):
        fila='| 1 | Ana | a | ACTIVE |\n| 2 | Bia | b | PENDING |\n| 3 | Ana | c | PENDING |\n'
        with self.assertRaises(ValueError):
            sincronizar_fila(CP,fila)

class PortfolioAuraly(unittest.TestCase):
    def portfolio(self):
        # 2026-09-20: contrato Puzzle. Uma acao estrutural preservada do hook do
        # video modelo e 10 variacoes trocando UMA variavel cada. Sem familias.
        # 2026-09-22: Puzzle com degrau. Topo declara peca viral e degrau; HOOK 1 e o controle.
        # 2026-09-23: as 10 so existem na rodada de variacao, sobre um video ja validado.
        partes = ['Rodada: VARIACAO',
                  'Base validada: producao exemplo, avatar Ana, performou no perfil',
                  'Acao estrutural: ela despeja algo sobre um objeto afetivo e a camada reage',
                  'Peca viral: o primeiro clipe da camada reagindo em macro',
                  'Degrau: DIFICULDADE - ela faz isso escondida no banheiro do trabalho']
        for numero in range(1, 11):
            partes += [
                ('HOOK %d - CONTROLE teste' if numero == 1 else 'HOOK %d - teste') % numero,
                'Variavel trocada: OBJETO - objeto %d' % numero,
                'Dominant anomaly: physical',
                'Cena: uma acao legivel acontece.',
                'Screen text: this sign found you',
                'Delayed meaning: o resultado so aparece no proximo beat',
                'Por que para o scroll: anomalia imediata.',
            ]
        return '\n'.join(partes)

    def falhas(self, texto, estrito=True):
        return [x for x in validar_portfolio_ganchos(texto, estrito) if x[0] == 'FALHA']

    def test_dez_variacoes_puzzle_valido(self):
        self.assertFalse(self.falhas(self.portfolio()))

    def test_reprova_contagem_errada(self):
        self.assertTrue(self.falhas(self.portfolio().replace('HOOK 10 - teste','HOOK 11 - teste')))

    def test_reprova_acao_estrutural_ausente(self):
        ruim = self.portfolio().replace(
            'Acao estrutural: ela despeja algo sobre um objeto afetivo e a camada reage', '', 1)
        self.assertTrue(self.falhas(ruim))

    def test_reprova_contrato_433_revogado(self):
        # O formato antigo em familias nao pode passar calado depois de 2026-09-20.
        ruim = 'PORTFOLIO AURALY 4/3/3\nFAMILY A - teste\n' + self.portfolio()
        self.assertTrue(self.falhas(ruim))

    def test_reprova_duas_variaveis(self):
        ruim = self.portfolio().replace('OBJETO - objeto 1','OBJETO - objeto 1 + LOCAL - cozinha')
        self.assertTrue(self.falhas(ruim))

    def test_reprova_degrau_ausente_no_estrito(self):
        ruim = self.portfolio().replace('Degrau: DIFICULDADE - ela faz isso escondida no banheiro do trabalho', '')
        self.assertTrue(self.falhas(ruim))
        self.assertFalse(self.falhas(ruim, estrito=False))

    def test_reprova_degrau_fora_da_escada(self):
        ruim = self.portfolio().replace('Degrau: DIFICULDADE', 'Degrau: GLITTER')
        self.assertTrue(self.falhas(ruim, estrito=False))

    def test_reprova_dois_controles(self):
        ruim = self.portfolio().replace('HOOK 2 - teste', 'HOOK 2 - CONTROLE teste')
        self.assertTrue(self.falhas(ruim, estrito=False))

    def test_reprova_sem_controle_no_estrito(self):
        ruim = self.portfolio().replace('HOOK 1 - CONTROLE teste', 'HOOK 1 - teste')
        self.assertTrue(self.falhas(ruim))

    def test_formato_historico_avisa_ou_falha(self):
        antigo = '## HOOK 1 - formato antigo\nCena: teste'
        self.assertEqual(validar_portfolio_ganchos(antigo, False)[0][0], 'AVISO')
        self.assertEqual(validar_portfolio_ganchos(antigo, True)[0][0], 'FALHA')

    def test_variacao_sem_base_validada_reprova(self):
        ruim = self.portfolio().replace('Base validada: producao exemplo, avatar Ana, performou no perfil', '')
        self.assertTrue(self.falhas(ruim, estrito=False))

    def test_sem_rodada_reprova_no_estrito(self):
        ruim = self.portfolio().replace('Rodada: VARIACAO', '')
        self.assertTrue(self.falhas(ruim))
        self.assertFalse(self.falhas(ruim, estrito=False))


class HookFielValidacao(unittest.TestCase):
    # 2026-09-23 (Luigi): validar antes de variar. Producao nova leva UM hook, fiel ao modelo.
    FIEL = '\n'.join([
        'Rodada: VALIDACAO',
        'Acao estrutural: ela despeja algo sobre um objeto afetivo e a camada reage',
        'Peca viral: o primeiro clipe da camada reagindo em macro',
        'HOOK 1 - FIEL - copia do modelo',
        'Cena: o hook do modelo plano a plano.',
        'Screen text: this sign found you',
        'Desvios obrigatorios: nenhum',
        'Delayed meaning: o resultado so aparece no proximo beat',
    ])

    def falhas(self, texto):
        return [x for x in validar_portfolio_ganchos(texto, True) if x[0] == 'FALHA']

    def test_hook_fiel_passa(self):
        self.assertFalse(self.falhas(self.FIEL))

    def test_validacao_com_dez_reprova(self):
        ruim = self.FIEL + '\nHOOK 2 - teste\nCena: outra.'
        self.assertTrue(self.falhas(ruim))

    def test_validacao_com_degrau_reprova(self):
        ruim = self.FIEL.replace('Rodada: VALIDACAO', 'Rodada: VALIDACAO\nDegrau: ESCALA - montanha')
        self.assertTrue(self.falhas(ruim))

    def test_desvios_nao_declarados_reprova(self):
        self.assertTrue(self.falhas(self.FIEL.replace('Desvios obrigatorios: nenhum', '')))

    def test_hook_sem_marca_fiel_reprova(self):
        self.assertTrue(self.falhas(self.FIEL.replace('HOOK 1 - FIEL - copia', 'HOOK 1 - copia')))

    def test_checkpoint_validacao_nao_espera_hook(self):
        cp = CP.replace('Current stage: PRODUCTION_COMPLETE', 'Current stage: WAITING_HOOK_SELECTION')
        self.assertTrue(any(x[0] == 'FALHA' and 'VALIDATION' in x[2] for x in verificar_estado(cp)))

    def test_checkpoint_variacao_exige_origem(self):
        cp = CP.replace('Round: VALIDATION', 'Round: VARIATION')
        self.assertTrue(any(x[0] == 'FALHA' and 'Validated from' in x[2] for x in verificar_estado(cp)))
        ok = cp.replace('Round: VARIATION', 'Round: VARIATION\nValidated from: exemplo, Ana, 120k views')
        self.assertFalse(any('Validated from' in x[2] for x in verificar_estado(ok)))

    def test_checkpoint_sem_round_reprova_no_estrito(self):
        cp = CP.replace('Round: VALIDATION\n', '')
        self.assertTrue(any(x[0] == 'FALHA' and 'Round' in x[2] for x in verificar_estado(cp, estrito=True)))

class CamadaVerbal(unittest.TestCase):
    # 2026-09-22: skill gancho-verbal. Topo com tese, sintoma-alvo e banco verbal;
    # o texto de tela repete frase do banco; frase banida reprova no estrito.
    TOPO = '\n'.join([
        'Tese: the jeans only close on a good day after forty',
        'Sintoma-alvo: jeans that only close on a good day',
        'Banco verbal:',
        '- "only close on a good day"',
        '- "after forty"',
        '- "half a lemon"',
        '- "the fat on a woman\'s legs"',
        '- "watch"',
        '',
        'HOOK 1 - CONTROLE',
        'Texto de tela: Jeans only close on a good day?',
    ])

    def falhas(self, texto):
        return [x for x in validar_camada_verbal(texto, True) if x[0] == 'FALHA']

    def test_topo_completo_passa(self):
        self.assertFalse(self.falhas(self.TOPO))

    def test_sem_banco_reprova_no_estrito_e_avisa_no_normal(self):
        texto = 'HOOK 1\nTexto de tela: legs after forty'
        self.assertTrue(self.falhas(texto))
        self.assertFalse([x for x in validar_camada_verbal(texto, False) if x[0] == 'FALHA'])

    def test_banco_curto_reprova(self):
        self.assertTrue(self.falhas(self.TOPO.replace('- "watch"\n', '')))

    def test_banco_sem_uso_reprova(self):
        self.assertTrue(self.falhas(self.TOPO.replace('Jeans only close on a good day?', 'New you soon')))

    def test_frase_banida_reprova(self):
        self.assertTrue(self.falhas(self.TOPO + '\nTexto de tela: His secret at 62'))

    def test_linha_que_documenta_a_proibicao_nao_conta(self):
        self.assertFalse(self.falhas(self.TOPO + '\nNunca usar "his secret" no gancho'))

class Registrar(unittest.TestCase):
    # 2026-09-22: registrar grava UMA publicacao; mesmo id substitui a coleta, nunca soma.
    def rodar(self, d, **kw):
        base = dict(producao='exemplo', avatar='walt', hook='K01', canal='instagram:@walt',
                    publicado_em='2026-09-01T10:00:00-03:00', coletado_em='2026-09-02T10:00:00-03:00',
                    objetivo='SALE', id=None, url=None, moeda=None, observacoes=None, metrica=[])
        base.update(kw)
        with mock.patch.object(go, 'CONTROLE', d), \
             mock.patch.object(go, 'biblioteca', lambda: [{'producao_id': 'exemplo', 'objetivo_declarado': 'SALE'}]), \
             mock.patch.object(go, 'atualizar', lambda: None):
            go.registrar(argparse.Namespace(**base))
        return json.loads((d / 'resultados.json').read_text())

    def test_registra_e_atualiza_sem_duplicar(self):
        with tempfile.TemporaryDirectory() as t:
            d = Path(t); (d / 'resultados.json').write_text('{"versao": 1, "publicacoes": []}')
            self.rodar(d, metrica=['visualizacoes=100'])
            doc = self.rodar(d, metrica=['visualizacoes=250'], coletado_em='2026-09-05T10:00:00-03:00')
            self.assertEqual(len(doc['publicacoes']), 1)
            self.assertEqual(doc['publicacoes'][0]['visualizacoes'], 250)

    def test_producao_desconhecida_nao_grava(self):
        with tempfile.TemporaryDirectory() as t:
            d = Path(t); (d / 'resultados.json').write_text('{"versao": 1, "publicacoes": []}')
            with self.assertRaises(ValueError):
                self.rodar(d, producao='nao_existe')
            self.assertEqual(json.loads((d / 'resultados.json').read_text())['publicacoes'], [])

class BaselineLinter(unittest.TestCase):
    # 2026-09-22: falhas antigas aceitas por pacote; qualquer falha nova continua contando.
    def separar(self, falhas, base, sem=False):
        with mock.patch.object(ce, '_BASELINE', base), mock.patch.object(ce, 'SEM_BASELINE', sem):
            return ce.separar_historicas('producao/pacote_antigo', falhas)

    def test_falha_da_baseline_vira_historica(self):
        novas, hist = self.separar([('bandeira', 'K01 sem bandeira', 'x:1')],
                                   {'pacote_antigo': ['bandeira|K01 sem bandeira']})
        self.assertEqual((len(novas), len(hist)), (0, 1))

    def test_falha_nova_em_pacote_antigo_continua_contando(self):
        novas, _ = self.separar([('bandeira', 'K01 sem bandeira', ''), ('travessao', 'T3 tem travessao', '')],
                                {'pacote_antigo': ['bandeira|K01 sem bandeira']})
        self.assertEqual([f[0] for f in novas], ['travessao'])

    def test_repeticao_alem_da_baseline_conta(self):
        f = ('bandeira', 'K01 sem bandeira', '')
        novas, hist = self.separar([f, f], {'pacote_antigo': ['bandeira|K01 sem bandeira']})
        self.assertEqual((len(novas), len(hist)), (1, 1))

    def test_sem_baseline_mostra_tudo(self):
        novas, _ = self.separar([('bandeira', 'K01 sem bandeira', '')],
                                {'pacote_antigo': ['bandeira|K01 sem bandeira']}, sem=True)
        self.assertEqual(len(novas), 1)

class Resultados(unittest.TestCase):
    def registro(self):
        return {'id':'p1','producao_id':'exemplo','avatar_id':'ana','hook_id':'K01','objetivo':'SALE','canal':'Instagram','publicado_em':'2026-01-01T10:00:00-03:00','coletado_em':'2026-01-02T10:00:00-03:00'}

    def validar(self,r):
        return validar_resultados({'versao':1,'publicacoes':[r]}, {'exemplo':'SALE'})

    def test_desconhecido_nao_e_zero(self):
        self.assertTrue(all(v is None for v in metricas({}).values()))
        self.assertEqual(metricas({'compras':0,'visitas_destino':10})['conversao'],0)
        self.assertIsNone(metricas({'compras':1,'visitas_destino':0})['conversao'])

    def test_denominadores_corretos(self):
        m=metricas({'visualizacoes':20,'impressoes':100,'cliques':5,'visitas_destino':4,'compras':1})
        self.assertEqual(m['ctr'],.05); self.assertEqual(m['conversao'],.25)

    def test_registro_valido_sem_metricas(self):
        self.validar(self.registro())

    def test_dados_invalidos(self):
        for patch in ({'compras':True},{'compras':1.5},{'custo':float('nan')},{'visualizacoes':-1},{'receita':10},{'objetivo':'GROWTH'},{'producao_id':'ausente'},{'coletado_em':'2025-01-01T10:00:00-03:00'},{'publicado_em':'2026-01-01'}):
            r=self.registro();r.update(patch)
            with self.subTest(patch=patch),self.assertRaises(ValueError): self.validar(r)

    def test_duplicatas(self):
        r=self.registro()
        with self.assertRaises(ValueError):
            validar_resultados({'versao':1,'publicacoes':[r,copy.deepcopy(r)]},{'exemplo':'SALE'})

if __name__=='__main__': unittest.main()
