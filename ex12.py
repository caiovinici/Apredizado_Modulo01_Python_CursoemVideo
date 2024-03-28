# Calculando desconto

print('Casas Bahia')
print('-'*40)
prod = str(input('Produto vendido: '))
preço = float(input(f'{prod} custa R$ '))
# Forma de somar desconto
desc = preço - (preço * 5 / 100)
print('-'*40)
print(f'O/A que custava R$ {preço:.2f}, na promoção com desconto de 5% vai custar R$ {desc:.2f}')

