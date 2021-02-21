#Faça um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letar'A'
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a útima vez

frase = input('Digite uma frase: ')
maiuscula = (frase.upper())
print('A letra "a" aparece {} vezes'.format(maiuscula.count('A')))
print('A letra "a" aparece na {} posição pela primeira vez.'.format(maiuscula.find('A')))
print('A letra "a" aparece tambem na {} posição pela ultima vez.'.format(maiuscula.find('A', -1, 0)))
#pode-se utilizar um argumento adicional que especifica o índice pelo qual ela deve começar sua procurar nesse caso usei o -1,
#que indica que ele deve começar a procurar pelo ultimo indice
#ou Ou ela pode receber dois argumentos adicionais que especificam o intervalo de índices:
#Ex.: frase.find('a', -1, -5)