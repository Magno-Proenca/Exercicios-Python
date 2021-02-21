#crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar.

numero = int(input('Digite um numero: '))
resto = numero % 2
if resto == 0:
    print('Este número é par.')
else:
    print('Este numero é impar.')