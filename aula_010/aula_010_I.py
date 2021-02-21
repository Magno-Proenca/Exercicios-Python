#Condições
'''if carro.esquerda():
    bloco True
else:
    bloco False'''

tempo=int(input('Qual a idade do seu carro: ')) #comandos do lado esquerdo da tela, sempre serão executados
if tempo <=3:
    print('Carro novo')#comandos indentados nem sempre serão executados
else:
    print('Carro velho')