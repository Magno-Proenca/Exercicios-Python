#Faça um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letar'A'
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a útima vez

frase = str(input("Digite uma frase: ")).upper().strip()#importante colocar o str para tranformar tudo em string
#deixando o upper ja no começo , eu deixo tudo em maiusculo.
print("A letra a 'a' aparece {} vezes na frase".format(frase.count("A")))
print("A letra 'a' aparece pela primeira vez na posição {}".format(frase.find("A")+1))#coloca +1 paraacertar as posições
print(" A letra 'A' aparece pela última vez na posição {}".format(frase.rfind("A")+1))#começa a procurar da direita

