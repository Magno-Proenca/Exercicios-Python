#para importar unicamente fa-se o comando ex.:from doce import
#agora para importar toda a biblioteca import da seguinte forma "import bebida"
#uma biblioteca que ja vem com o Python é a math que traz funcionalidades matematicas extras
#funcionaliades da biblioteca math, ceil, floor, trunc, pow, sqrt, factorial
import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igaul a {}'. format(num, math.ceil(raiz))) # ceil está arredondando para acima a raiz


