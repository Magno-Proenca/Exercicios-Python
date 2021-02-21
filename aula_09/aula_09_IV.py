#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
#Ex.: Digite um numero : 1834
#unidade:4
#dezena:3
#centena:8
#milhar:1
numero = input('Digite um número entre 0 à 9999: ')
print('Unidade: {}'.format(numero[3]))
print('Dezena: {}'.format(numero[2]))
print('Centena: {}'.format(numero[1]))
print('Milhar: {}'.format(numero[0]))

