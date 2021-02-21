#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
#Ex.: Digite um numero : 1834
#unidade:4
#dezena:3
#centena:8
#milhar:1
numero = int(input("Digite um nùmero de 0 à 9999: "))
unidade = numero // 1 % 10
dezena = numero // 10 % 10 #para melhor entender divido p.ex.: 1234/10, e pego so a parte inteira que 123 e dividio por 10,novamente monstrando o resto
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print("Unidade: {}".format(unidade))
print("Dezena: {}".format(dezena))
print("Centena: {}".format(centena))
print("Milhar: {}".format(milhar))

