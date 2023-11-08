from funcoes import filtra
from funcoes import inicializa
from funcoes import indica_posicao
from banco_palavras import PALAVRAS
import time

palavras = ['arroz', 'menor', 'maior', 'banco', 'carro','barro','banana','macaco']
filtro = filtra(PALAVRAS,5)

sorteada = inicializa(filtro)['sorteada']
tentativas = len(sorteada)+1
qt_letras = len(sorteada)
especuladas = []
espec = ''

print(' =========================== ')
print('|                           |')
print('| Bem-vindo ao Insper Termo |')
print('|                           |')
print(' ==== Design de Software === ')
print('Comandos: desistir, dica')
print(' Regras:\n')
print('  - Você tem 6 tentativas para acertar uma palavra aleatória de 5 letras.')
print('  - A cada tentativa, a palavra testada terá suas letras coloridas conforme:')
print('    . Azul   : a letra está na posição correta;')
print('    . Amarelo: a palavra tem a letra, mas está na posição errada;')
print('    . Cinza: a palavra não tem a letra.')
print('  - Os acentos são ignorados;')
print('  - As palavras podem possuir letras repetidas.\n')
print('Sorteando uma palavra...')
time.sleep(1.5)
print('Já tenho uma palavra! Tente adivinhá-la!\n')
print('Você tem',tentativas, 'para acertar uma palavra aleatória de 5 letras')

print('Sorteando uma palavra...\n')
print('Você tem 6 tentativas para acertar uma palavra aleatória de 5 letras')
print('Você tem',tentativas,'tentativa(s)!')


print(sorteada)
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
     print('\n',especuladas,'\n')
     tentativas -= 1

     if tentativas == 0:
          print('Você perdeu! A palavra era: ',sorteada)
          break
     
     print('Você tem ',tentativas,'tentativa(s)!')