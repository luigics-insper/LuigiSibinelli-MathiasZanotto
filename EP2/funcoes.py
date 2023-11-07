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
