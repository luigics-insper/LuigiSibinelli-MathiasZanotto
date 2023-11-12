from funcoes import filtra
from funcoes import inicializa
from funcoes import indica_posicao
from banco_palavras import PALAVRAS
import time
import random

#Cores utilizadas
class Color:
    reset = '\033[0m'
    azul = '\033[34m'
    amarelo = '\033[33m'
    cinza = '\033[30m'

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
print('    . \033[94mAzul\033[0m  : a letra está na posição correta;')
print('    . \033[93mAmarelo\033[0m: a palavra tem a letra, mas está na posição errada;')
print('    . \033[90mCinza\033[0m: a palavra não tem a letra.')
print('  - Os acentos são ignorados;')
print('  - As palavras podem possuir letras repetidas.\n')

#Jogo do termo
while True:
    print('Sorteando uma palavra...')
    time.sleep(0.7)
    inicio = time.time()
    print('Você tem 6 tentativas para acertar uma palavra aleatória de 5 letras')
    print('Já tenho uma palavra! Tente adivinhá-la!\n')

    filtro = filtra(PALAVRAS,5)
    sorteada = inicializa(filtro)['sorteada']
    tentativas = len(sorteada)+1
    qt_letras = len(sorteada)
    especuladas = []
    opcao = ''

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
        especulada_letras = list(especulada)
        posicoes = indica_posicao(sorteada, especulada)
        
        #Comando de desistência
        if especulada == 'desisto':
            while opcao != 's' or opcao != 'n':
                opcao = input('\nQuer jogar novamente? (s/n) ')
                if opcao == 's':
                    i = 7
                    break
                elif opcao == 'n':
                    print('Obrigado por jogar!')
                    break
        if opcao == 'n':
            break
        if opcao == 's':
            print('')
            break

        #Comando de dica
        if especulada == 'dica':
            print(sorteada[random.randint(0,len(sorteada)-1)])
            continue

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

        string = ''
        for index, posicao in enumerate(posicoes):
            if posicao == 0:
                letra = '\033[94m' + especulada[index] + '\033[0m'
            elif posicao == 1:
                letra = '\033[93m' + especulada[index] + '\033[0m'
            else:
                letra = '\033[90m' + especulada[index] + '\033[0m'
            string += letra

        especulada = string
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
                l6 += ' ' + letra + ' |'

        tabela = print('  --- --- --- --- --- \n',l1,'\n' '  --- --- --- --- --- \n',l2,'\n' '  --- --- --- --- --- \n',l3,'\n' '  --- --- --- --- --- \n',l4,'\n' '  --- --- --- --- --- \n',l5,'\n' '  --- --- --- --- --- \n',l6,'\n' '  --- --- --- --- --- \n')
        
        #Condição de vitória
        if especulada == sorteada:
            fim = time.time()
            tempo_jogado = fim-inicio
            if tempo_jogado >= 60:
                print(f'Você acertou em {((fim-inicio)//60):.0f} minuto(s) e {abs((fim-inicio)-(fim-inicio//10*10)):.0f} segundo(s)!')
            else:
                print(f'Você acertou em {(fim-inicio):.0f} segundos!')
            while opcao != 's' or opcao != 'n':
                opcao = input('Quer jogar novamente? (s/n) ')
                if opcao == 's':
                    break
                elif opcao == 'n':
                    print('Obrigado por jogar!')
                    break
        if opcao == 'n':
            break
        if opcao == 's':
            print('')
            break

        tentativas -= 1
        i += 1
        if tentativas > 0:
            print('Você tem ',tentativas,'tentativa(s) faltando!')

        #condição de derrota
        if tentativas <= 0:
            print('Você perdeu! A palavra era:',sorteada)
            while opcao != 's' or opcao != 'n':
                opcao = input('Quer jogar novamente? (s/n) ')
                if opcao == 's':
                    break
                elif opcao == 'n':
                    print('Obrigado por jogar!')
                    break
        if opcao == 'n':
            break
        if opcao == 's':
            print('')
            break
    if opcao == 'n':
        break