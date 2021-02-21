#um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')
lista = [nome1, nome2, nome3, nome4]
#eu não conhecia esta funcionalidade de ter que fazer uma lista para funcionar a função random
esc = random.choices(lista)
print('O nome escolhido foi {}'.format(esc))
