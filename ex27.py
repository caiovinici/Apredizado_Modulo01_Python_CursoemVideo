# Primeiro e último nome de uma pessoa

n = str(input('Informe seu nome completo: ')).strip()
nome = n.split()
print(f'Muito prazer em te conhecer {nome[0]}')
print(f'\nSeu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')
