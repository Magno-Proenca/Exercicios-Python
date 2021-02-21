#Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor.
numero = float(input('Digite um numero: '))
numeroII = float(input('Digite outro numero: '))
numeroIII = float(input('Digite outro numero: '))

if numero > numeroII:
    maior = numero
else:
    maior = numeroII
if maior > numeroIII:
    print('O maior número é o {}'.format(maior))
else:
    print('O maior numero é o {}'.format(numeroIII))
if numero < numeroII:
    menor = numero
else:
    menor = numeroII
if menor < numeroIII:
    print('Menor numero é o {}'.format(menor))
else:
    print('Menor numero é o {}'.format(numeroIII))