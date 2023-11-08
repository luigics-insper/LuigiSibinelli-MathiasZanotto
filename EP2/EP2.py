from funcoes import filtra
from funcoes import inicializa
from funcoes import indica_posicao
from banco_palavras import PALAVRAS

palavras = palavras = ['arroz', 'menor', 'maior', 'banco', 'carro','barro','banana','macaco']

sorteada = inicializa(palavras)['sorteada']
tentativas = len(sorteada)+1
qt_letras = len(sorteada)
especuladas = []
espec = ''

print('Você tem',tentativas, 'tentativas para acertar uma palavra aleatória de',qt_letras,'letras')
print('Sorteando uma palavra...\n')
print('Você tem',tentativas,'tentativa(s)!')

filtro = filtra(PALAVRAS,qt_letras)

while espec != sorteada:
     '''
     print('A palavra sorteada é',sorteada,'\n') -- para descobrir a palavra sorteada
     '''

     espec = input('Qual é seu palpite? \n')

     if espec not in PALAVRAS:
          print('Palavra desconhecida')
          continue
     if espec not in filtro:
          print('Apenas palavras de',qt_letras,'letras!\n')
          continue
     if espec == sorteada:
          print('Voce acertou')
          break
     if espec in especuladas:
          print('Palavra já testada.')
          continue

     especuladas.append(espec)
     print('\n',especuladas)
     tentativas -= 1

     if tentativas == 0:
          print('Você perdeu! A palavra era: ',sorteada)
          break
     
     print('Você tem ',tentativas,'tentativa(s)!')