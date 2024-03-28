# Par ou Ímpar ?

número = int(input('Ímpar ou Par ? '))
resultado = número % 2

if resultado == 0:
    print(f'{número} é Par')
else:
    print(f'{número} é Ímpar')
    