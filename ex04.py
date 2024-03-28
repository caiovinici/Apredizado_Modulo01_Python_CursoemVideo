# Disseando uma variável

a = input('Digite algo para saber seus valores: ')
#type - o tpipo primitivo da str
print('O tipo primitivo desse valor é ', type(a))
#isspace - identifica espaços
print('Só tem espaços?', a.isspace())
#isnumeric - identifica um número
print('É um número ?', a.isnumeric())
#isalpha - identifica se é alfabetico
print('É alfabetico?', a.isalpha())
#isalnum - identifica se é alfanumérico
print('É alfanumérico?', a.isalnum())
#isupper - identifica letras maiúsculas
print('Está em maiúsculas?', a.isupper())
#islower - identifica letras minúsculas
print('Está em minúsculas?', a.islower())
print('Está capitalizada?', a.istitle())

