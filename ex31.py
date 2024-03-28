# Custo da  viagem por KM

distancia = float(input('Distância da corrida: '))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print(f'A sua viagem de \033[1m{distancia}\033[m custará R$ \033[1m{preço:.2f}\033[m')
