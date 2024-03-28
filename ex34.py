# Aumentos multiplos

s = float(input('\033[4mSálario do funcionario R$\033[m '))

from time import sleep
sleep(1.5)
print('==' * 25)

if s <= 1250:
    novo_salario = s + (s * 15 / 100) # 15% forma de somar %
else:
    novo_salario = s + (s * 10 / 100) # 10% forma de somar %
print(f'Quem ganhava R$ \033[32m{s:.2f}\033[m passa a ganhar R$ \033[32m{novo_salario:.2f}\033[m')
