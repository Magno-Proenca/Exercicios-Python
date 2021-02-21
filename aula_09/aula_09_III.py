#Aula de Exercicio 22
#Crie um programa que leia o nome completo de uma pessoa e mostre
#o nome com todas as letras maiusculas
#o nome com todas a s letras minusculas
#quantas letras no total (sem considerar espaços)
#quantas letras tem o primeiro nome

nome = str(input('Digite seu nome: '))
print('O seu nome completo em letras maiúscula é {}'.format(nome.upper()))
print('O seu nome completo em letras minuscula é {}'.format(nome.lower()))
print('O nome completo tem um total de {} letras'.format(len(nome.strip()) - nome.count(' ')))
#como se fosse uma operção mateamtica eu subtraio um metodo do outro (nome.strip()) - nome.count(' ')
nomeII = nome.split()
print('O primeiro nome tem um total de {} letras'.format(len(nomeII[0])))
