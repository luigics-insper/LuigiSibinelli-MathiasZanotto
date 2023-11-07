from funcoes import filtra
from funcoes import inicializa
from funcoes import indica_posicao

palavras = ['arroz', 'menor', 'maior', 'banco', 'carro','barro']

sorteada = inicializa(palavras)['sorteada']
tentativas = inicializa(palavras)['tentativas']
qt_letras = inicializa(palavras)['n']
especuladas = []
espec = ''

print('Você tem',tentativas, 'para acertar uma palavra aleatória de ',qt_letras,'letras')
print('Sorteando uma palavra...\n')
print('Você tem ',inicializa(palavras)['tentativas'],'tentativa(s)!')

while espec != sorteada:
     #print('A palavra sorteada é',sorteada,'\n')
     espec = input('Qual é seu palpite? ')
     especuladas.append(espec)
     if espec == sorteada:
          print('Voce acertou')
          break

     tentativas -= 1

     if tentativas == 0:
          print('Você perdeu! A palavra era: ',sorteada)
          break
     
     print('Você tem ',tentativas,'tentativa(s)!')