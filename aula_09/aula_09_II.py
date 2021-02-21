#transformação
#replace vai susbstituir uma palavra que eu desejar por outra
#lembrando que as strings são imutaveis, e a unica forma de substituir uma string é desta forma
frase = 'Curso em video Python'
print(frase.replace('Python','Android'))
#troca toda a frase por letra maiúscula
print(frase.upper())

#troca toda a frase por letra minúscula
print(frase.lower())

#capitalize significa que todos caracteres serão jogados para minusculos e mantendo somente a primeira letra maiuscula
print(frase.capitalize())

#title transforma todos o primeiros caracteres de cada palavra em maiúsculo
print(frase.title())

#vamos mudar a string para 'Aprenda Python'
frase = ('   Aprenda Python  ')
#remove todos os espaços inuteis a função strip
print(frase.strip())

#o rstrip remove os espaços inuteis do lado direito da string e o lstrip retira da esquerda
print(frase.rstrip())

#split é feito em seus espaços e vai ocorrer um divisão dentro da string considerando seus espaços
#cada palavra recebe uma indexação nova, cada palavra gera uma lista nas em cada cadeia de caractere
fraseI = frase.split()
print(fraseI)
#de forma analoga ao split, eu fiz o split , agora eu faço a junção disto agora
#se eu tenho o nome separado em lista, eu agora uso o join que é para juntar uma coisa na outra
#o '-' antes da função join significa que estou pedindo para utilizar esse tracinho entre os splits de caracteres
print('-'.join(fraseI))


