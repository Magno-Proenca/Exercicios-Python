#Crie uma pessoa que leia o nome de uma pessoa e diga se
#ela tem 'Silva' no nome.
nome = input('Digite um nome: ')
nomeII = (nome.upper())
silva = ('SILVA' in nomeII)
print('O nome Silva é {} no seu nome'.format(silva))