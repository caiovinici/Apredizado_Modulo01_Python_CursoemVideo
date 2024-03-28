# Sorteando um item na lista

from random import choice
n1 = str(input('Primeiro aluno(a): '))
n2 = str(input('Segundo alno(a): '))
n3 = str(input('Terceiro aluno(a): '))
n4 = str(input('Quarto aluno(a): '))
# lista = [o que vai na lista]
lista = [n1, n2, n3, n4]

#Choice - Retorna um elemento aleatório da sequência não vazia seq.
escolhido = choice(lista)
print(f'O aluno(a) escolhido foi {escolhido}')
