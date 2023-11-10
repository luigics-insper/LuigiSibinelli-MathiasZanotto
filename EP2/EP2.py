from funcoes import filtra
from funcoes import inicializa
from funcoes import indica_posicao
from banco_palavras import PALAVRAS
from rich.console import Console
console = Console()
import time

#VARIAVEIS
filtro = filtra(PALAVRAS,5)
sorteada = inicializa(filtro)['sorteada']
tentativas = len(sorteada)+1
qt_letras = len(sorteada)
especuladas = []
espec = ''

# REGRAS / INICIO
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
time.sleep(1.2)
print('Você tem',tentativas, 'tentativas para acertar uma palavra aleatória de 5 letras')
print('Já tenho uma palavra! Tente adivinhá-la!\n')




print('A palavra sorteada é',sorteada,'\n') # -- para descobrir a palavra sorteada

l1 = '|   |   |   |   |   |'
l2 = '|   |   |   |   |   |'
l3 = '|   |   |   |   |   |'
l4 = '|   |   |   |   |   |'
l5 = '|   |   |   |   |   |'
l6 = '|   |   |   |   |   |'

i = 0
while i < 6:
    especulada = input('Qual é seu palpite? \n')
     
    if especulada == 'desisto':
        while opcao != 's' or opcao != 'n':
            opcao = input('Quer jogar novamente? (s/n) ')
            if opcao == 's':
                i = 6
                break
            elif opcao == 'n':
                print('Obrigado por jogar!')
                break

    if especulada not in PALAVRAS:
          print('Palavra desconhecida')
          continue
    elif especulada not in filtro:
          print('Apenas palavras de',qt_letras,'letras!\n')
          continue
    elif especulada in especuladas:
          print('Palavra já testada.')
          continue
    especuladas.append(especulada)
    if i == 0:
        l1 = '|'
        for letra in especulada:
            l1 += ' ' + letra + ' |'
    if i == 1:
        l2 = '|'
        for letra in especulada:
            l2 += ' ' + letra + ' |'
    if i == 2:
        l3 = '|'
        for letra in especulada:
            l3 += ' ' + letra + ' |'
    if i == 3:
        l4 = '|'
        for letra in especulada:
            l4 += ' ' + letra + ' |'
    if i == 4:
        l5 = '|'
        for letra in especulada:
            l5 += ' ' + letra + ' |'
    if i == 5:
        l6 = '|'
        for letra in especulada:
            l5 += ' ' + letra + ' |'

    tabela = print('  --- --- --- --- --- \n',l1,'\n' '  --- --- --- --- --- \n',l2,'\n' '  --- --- --- --- --- \n',l3,'\n' '  --- --- --- --- --- \n',l4,'\n' '  --- --- --- --- --- \n',l5,'\n' '  --- --- --- --- --- \n',l6,'\n' '  --- --- --- --- --- \n')
    
    if espec == sorteada:
        print('Você acertou!')
        opcao = input('Quer jogar novamente? (s/n) ')
        while opcao != 's' or opcao != 'n':
                print('Coloque "s" ou "n"!\n')
                opcao = input('Quer jogar novamente? (s/n) ')
                if opcao == 's':
                    continue
                elif opcao == 'n':
                    print('Obrigado por jogar!')
                    break

    '''for result in indica_posicao(sorteada,especulada):
        if result == 0:
            print('pos e letra certa')
        elif result == 1:
            print('letra certa, pos errada')
        elif result == 2:
            print('letra e pos erradas')'''
    tentativas -= 1
    i += 1
    print('Você tem ',tentativas,'tentativa(s) faltando!')

    if tentativas == 0:
        print('Você perdeu! A palavra era: ',sorteada)
        opcao = input('Quer jogar novamente? (s/n) ')
        while opcao != 's' or opcao != 'n':
            opcao = input('Quer jogar novamente? (s/n) ')
            if opcao == 's':
                i = 6
                break
            elif opcao == 'n':
                print('Obrigado por jogar!')
                break