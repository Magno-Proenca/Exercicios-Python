#faça um programa que leia algo pelo teclado e mostre o seu tipo primitivo e todas as informações possiveis sobre ela
n1 = input('Digite algo: ')
print('É alfabetico: ', n1.isalpha())
print('É alfanumerico: ', n1.isalnum())
print('É numérico: ', n1.isnumeric())
print('Está em caixa alta; ', n1.isupper())

