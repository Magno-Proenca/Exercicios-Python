#Faça um programa que leia um ano qualquer e mostre se ele é Bissexto
ano = int(input('Digite o ano para saber se é bissexto: '))
bissexto = ano % 4
if bissexto == 0:
    print('O ano de {} é bissexto'. format(ano))
else:
    print('O ano de {}, não é bissexto'.format(ano))
print('Bye, bye Leticia')