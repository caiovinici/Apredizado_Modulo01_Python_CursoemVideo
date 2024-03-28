# Jogo da adivinhação v.1

from random import randint
from time import sleep

comp = randint(0, 100) # Faz o pc sortear um número

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 100. Tente adivinha!')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei?'))
print(f'P R O C E S S A N D O . . .')
# sleep() - Faz ter espera para processar o resto do código (segundos)
sleep(2)
if jogador == comp:
    print('Parabéns! Você conseguiu me vencer.')
else:
    print(f'Ganhei! Eu pensi no número {comp} e não no {jogador}')
