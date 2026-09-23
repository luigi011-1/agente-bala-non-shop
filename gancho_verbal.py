"""Camada verbal do gancho, todos os angulos (skill gancho-verbal, 2026-09-22).

O Puzzle com degrau decide o que se VE no gancho (auraly_validacao.validar_portfolio_ganchos).
Aqui se confere o que se LE e se OUVE: o topo do arquivo de ganchos declara tese, sintoma-alvo e
banco verbal com frases literais do roteiro, e nenhuma frase banida aparece nas variacoes.

Pacote anterior a 2026-09-22 nao tem o topo: avisa no modo normal e so reprova no --estrito,
o mesmo criterio usado quando a peca viral e o degrau entraram no contrato.
"""
import re
import unicodedata

MIN_BANCO = 5

# Varredura da skill: sentimental, consequencia eufemistica e beneficio de enfeite.
BANIDAS = [
    "reaches for me", "reaching for me", "you're back", "i cried", "made me cry",
    "wants me again", "the man i married", "back to the man", "feel like myself again",
    "hasn't let me sleep", "kept me up all night", "keeps me up all night", "walking funny",
    "canceling morning plans", "neighbors think we're newlyweds", "i'm exhausted",
    "his secret", "her secret", "the secret", "the same question", "what he does",
    "what she does", "what changed", "the reason", "what they don't want you to know",
]
# Linha que documenta a regra (cita a frase para proibir) nao conta como uso.
RE_DOC = re.compile(r"banid|proibid|banned|nunca|never|reprova|evitar|avoid", re.I)
RE_ROTULO = lambda nome: re.compile(
    r"^\s*(?:[-*]\s*)?(?:\*\*)?(?:" + nome + r")(?:\*\*)?\s*:\s*(.*?)\s*$", re.M | re.I)
RE_TESE = RE_ROTULO(r"Tese|Thesis")
RE_SINTOMA = RE_ROTULO(r"Sintoma[- ]alvo|Target symptom")
RE_BANCO = RE_ROTULO(r"Banco verbal|Vocabulary bank|Script phrases")
RE_ASPAS = re.compile(r"[\"“]([^\"”\n]{3,})[\"”]")


def _norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return s.replace("’", "'").replace("‘", "'")


def _frases_do_banco(texto, m):
    """Frases entre aspas na linha do rotulo e nas linhas de lista logo abaixo.

    Devolve as frases e o indice onde o bloco do banco termina."""
    frases = RE_ASPAS.findall(m.group(1))
    fim = m.end()
    for linha in texto[m.end():].split("\n")[1:]:
        s = linha.strip()
        if s and not s.startswith(("-", "*", "•")) and not RE_ASPAS.match(s):
            break
        if not s and frases:
            break
        frases += RE_ASPAS.findall(s)
        fim += len(linha) + 1
    return [f.strip() for f in frases if f.strip()], fim


def validar_camada_verbal(texto, estrito=False, loc="GANCHOS_VISUAIS.md"):
    issues = []
    add = lambda nivel, msg: issues.append((nivel, "gancho-verbal", msg, loc))
    if not texto:
        return issues
    novo = "FALHA" if estrito else "AVISO"

    faltando = [n for n, r in (("Tese", RE_TESE), ("Sintoma-alvo", RE_SINTOMA)) if not r.search(texto)]
    if faltando:
        add(novo, "Falta %s no topo (skill gancho-verbal, PASSO 0)." % " e ".join(faltando))

    m = RE_BANCO.search(texto)
    if not m:
        add(novo, 'Falta "Banco verbal:" com %d frases literais do roteiro aprovado.' % MIN_BANCO)
    else:
        frases, fim = _frases_do_banco(texto, m)
        if len(frases) < MIN_BANCO:
            add(novo, "Banco verbal com %d frase(s) entre aspas; o minimo e %d."
                % (len(frases), MIN_BANCO))
        else:
            fora = _norm(texto[fim:])
            usadas = [f for f in frases if _norm(f) in fora]
            if not usadas:
                add(novo, "Nenhuma frase do banco verbal aparece nas variacoes: "
                          "o texto de tela tem que repetir palavras da fala (sincronia).")
            else:
                add("OK", "banco verbal com %d frases, %d usadas nas variacoes"
                    % (len(frases), len(usadas)))

    for n, linha in enumerate(texto.splitlines(), 1):
        if RE_DOC.search(linha):
            continue
        baixa = _norm(linha)
        for frase in BANIDAS:
            if re.search(r"(?<![a-z])" + re.escape(frase) + r"(?![a-z])", baixa):
                issues.append((novo, "gancho-verbal",
                               "frase banida '%s' (sentimental, eufemistica ou de enfeite)" % frase,
                               "%s:%d" % (loc, n)))
    return issues
