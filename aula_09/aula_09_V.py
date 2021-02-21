#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'
cidade = input('Digite o nome de sua cidade: ')
santo = (cidade.upper())
palavra = ('SANTO' in santo)
print('A palavra Santo é {} no nome da cidade.'.format(palavra))