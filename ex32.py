# Ano Bissexto

from datetime import date
ano = int(input('Que ano deseja analisar ? Coloque o 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year # pega o ano atual da maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano \033[4m{ano}\033[m é BISSEXTO')
else:
    print(f'O ano \033[4m{ano}\033[m não é BISSEXTO')
