from time import sleep
from random import randint
from datetime import date

atual = date.today().year

nome = input('Digite o seu nome: ').title()
nascimento = input('Ano de nascimento: ').title()

try:
    nasc = int(nascimento)
    idade = atual - nasc


    print(f'Seu nome e {nome} voce tem {idade}')

    sleep(2)
    if idade == 18:
        print(f'Com seus {idade} anos voce teve um acidente tragico')
    elif idade > 18:
        print(f'''
        Ja faz mais de 10 anos do seu acidente
        Durante todo esse tempo voce esta se mantendo forte
        Sempre tentou e tentou algo para voce e sua familia
        Por favor não desista, confia no processo
        Deus Esta comtigo, confia no processo''')
    else:
        print(f'Hora de Desistir')

except ValueError as erro:
    print(f'Tivemos um erro: {erro}')