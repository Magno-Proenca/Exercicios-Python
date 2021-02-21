#faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente
#Ex.: Ana Maria de Souza
#primeiro=Ana
#último=Souza
nome = str(input('Digite o seu nome: ')).strip()
nomeI = (nome.split())
print('Seu primeiro nome é {}'.format(nomeI[0]))
#print("Seu ultimo nome é {}".format(nomeI[-1])
#eu fiz a linha de cima e o Gustavo Guanabara a linha abaixo
print("O seu sobrenome é {}".format(nomeI[len(nomeI)-1]))
