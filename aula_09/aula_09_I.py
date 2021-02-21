#String, cadeia de caracteres e cadeia de textos, são as mesmas coisas
frase = ' Curso em Video Python ' #cada letra desta string ocupa um microespaço no programa, e é dividida por números
print(frase)
fatia = frase[9:14]
print(fatia)
fatia = frase[9:21:2] #vai do 9 ao 21 de 2 em 2
print(fatia)
fatia = frase[:5]#aqui ele entende que vai desde o caractere 0
print(fatia)
#len vem de lenght, ele mostra o comprimento da frase, essa frase tem 21 caracteres, ele tendo esses 21 microespaço
print(len(frase))#ou eu poderia criar uma variavel para atribuir a funcionalidade
# len e depois manda-la printa-la na linha seguinte
#ex.: fatia = len(frase)
#     print(fatia)
#posso mesclar  dois métodos mandando deixar tudo em maiúsculo e contar a letra 'O' ao mesmo tempo
print(frase.upper().count('O'))
#posso mesclar função com metodo, Ex.: len com strip
print(len(frase.strip()))

# count manda o programa contar quantas vezes aparece determinada letra e o 0 e o 13 do
#exemplo indica que a letra será contada nesse periodo indicado (do 0 ao 13)
fatia = frase.count('o',0,13)
print(fatia)
# find me diz qual posição eu encontro a palavra determinada, nesse caso na letra 11
# se retornar o numero -1 é por que a string não existe
fatia = frase.find('deo')
print(fatia)
# in frase serve para perguntar se em uma variável em que uma string está inserida existe
#determinada palavra que eu queira encontrar, find não é uma funcionalidade é um metodo
print('curso' in frase)

