# Catetos e Hipotenusa

from math import hypot
co = float(input('Digite o número do cateto oposto: '))
ca = float(input('Digite o cateto adiacente: '))
#Hypot - Retorna a norma euclidiana, sqrt(sum(x**2 for x in coordinates)).
hi = hypot(co, ca)
print(f'A hipotenusa vai medir {hypot(hi):.2f}')
