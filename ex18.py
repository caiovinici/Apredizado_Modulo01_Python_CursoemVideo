# Seno, Cosseno e Tangente

from math import radians, sin, tan, cos
ang = float(input('Digite o ângulo que deseja: '))

# radians - Converte o ângulo x de graus para radianos.
# sin - Retorna o seno de x radianos.
seno = sin(radians(ang))
print(f'O ângulo de {ang} tem o SENO de {seno:.2f}')

# cos - Retorna o cosseno de x radianos.
cosse = cos(radians(ang))
print(f'O ângulo de {ang} tem o COSSENO de {cosse:.2f}')

# tan - Retorna o tangente de x radianos.
tang = tan(radians(ang))
print(f'O ângulo de {ang} tem a TANGENTE de {tang:.2f}')

