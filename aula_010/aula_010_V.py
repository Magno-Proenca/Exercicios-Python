#escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça
#para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
#o programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
numero = int(input('Digite um numero de 0 à 5: '))
escolhido = randint(0, 5)
if numero == escolhido:
    print('Parabéns você acertou o numero escolhido foi {}!'.format(escolhido))
else:
    print('Você errou ! Melhor sorte na proxima vez!')
print('Até a próxima!')
