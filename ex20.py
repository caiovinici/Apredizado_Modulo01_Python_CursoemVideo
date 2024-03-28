#Sorteando uma ordem na lista

from random import shuffle
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]

#shufle - Embaralha a sequência x internamente. Dentro de lista
shuffle(lista)
print(f'\nA ordem de apresentação será ')
print(lista)
