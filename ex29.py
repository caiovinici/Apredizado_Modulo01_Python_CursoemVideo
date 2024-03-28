# Radar eletrônico

from time import sleep
print('*=*' * 15)
print(' \033[1;33;40m----- DETRAN - SISTEMAS DE MULTAS -----\033[m ')

print('*=*' * 15)

velocidade = float(input('Velocidade atingida pelo veículo: '))
sleep(1.5)

# if - se
if velocidade > 80:
    print(f'Você excedeu o limite permitido na via \033[4;31m80km/h.\033[m')
    multa = (velocidade-80) * 7
    print(f'A multa é do valor de \033[1;32mR$ {multa:.2f}\033[m.')
# else - se nao
else:
    print('Tenha sempre atenção ao volante!')
