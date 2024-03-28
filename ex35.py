# Analisando Trângulo v1.0

r1 = float(input('\033[4mPrimeio segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento\033[m: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[1;32mFORMAM\033[m um triângulo')
else:
    print('os segmentos acima \033[1;31mNÂO\033[m forma um triângulo')
