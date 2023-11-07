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

def indica_posicao(sorteada,especulada):
    out = []
    sort = {}
    espec = {}
    i = 0
    for letra in sorteada:
        if i not in sort.keys():
            sort[i] = letra
        i += 1
    i = 0
    for letra in especulada:
        if i not in espec.keys():
            espec[i] = letra
        i += 1
    for letra in espec:
        if espec.get(letra) not in sort.values():
            out.append(2)
        elif espec.get(letra) == sort.get(letra):
                out.append(0)
        elif espec.get(letra) != sort.get(letra) and letra in sort:
                out.append(1)
    return out

#######################

