# Maior & Menor valores

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

# Verificando número MENOR
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Verificando númenor MAIOR
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('==' * 15)
print(f'O menor número é \033[4;31m{menor}\033[m')
print(f'O maior número é \033[4;32m{maior}\033[m')

