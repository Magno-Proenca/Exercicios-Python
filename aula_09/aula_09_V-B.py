#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'
cidade = input("Digite o nome de uma cidade que contenha a palavra 'Santo': ").strip()#coloca-se strip para eçiminar os espaços
santo = (cidade[0:5].upper() == "SANTO")#o .upper joga para maiusculo o que foi escrito e compara se é igual a SANTO
print("A palavra 'Santo' é {} no nome desta cidade".format(santo))