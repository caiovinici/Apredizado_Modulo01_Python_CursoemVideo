# Procurando uma string dentro de outra

nome = str(input('Informe seu nome completo: ')).strip()
# In se tem SILVA na vareavel nome
print(f'Seu nome tem Silva? {'SILVA' in nome.upper()}')
