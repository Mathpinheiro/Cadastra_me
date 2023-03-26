# Projeto 1
import datetime
import random


nome = input('Digite o nome: ')

idade = int(input('Digite a sua idade: '))

cadastro = format(datetime.date.today(),  '%d/%m/%Y')

cartoes = ['R$ 50,00', 'R$250,00', 'R$120,00']
sorteio = random.choice(cartoes)


boas_vindas = f'Olá {nome}, seu registro foi concluído com sucesso no dia {cadastro}. \n\
    Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {sorteio}.'

print(boas_vindas)
