#bibliotecas
import random 

#funções
def filtra(lista,numletras):
    out = []
    for palavra in lista:
        if len(palavra) == numletras:
            if palavra.lower() not in out:
                out.append(palavra.lower())
    return out

def inicializa(palavras):
    out = {}
    n = len(palavras[0])
    sorteada = random.choice(palavras)
    espec = []
    tentativas = n+1
    out['n'] = n
    out['sorteada'] = sorteada
    out['especuladas'] = espec
    out['tentativas'] = tentativas
    return out

def indica_posicao(sorteada, especulada):
    posicao = []
    if len(sorteada) != len(especulada):
        return posicao
    i = 0
    while i < len(sorteada):
        if especulada[i] == sorteada[i]:
            posicao.append(0)
        elif especulada[i] in list(sorteada):
            posicao.append(1)
        elif especulada[i] not in list(sorteada):
            posicao.append(2)
        i += 1
    return posicao