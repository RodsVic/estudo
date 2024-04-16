'''
## Verificar conteúdo da String

Escreva um programa em Python para verificar se uma string contém apenas
um determinado conjunto de caracteres (neste caso, a-z, A-Z e 0-9).
import re

def regex(text):
    pattern = re.compile(r'[^a-zA-Z0-9]')
    text = pattern.search(text)
    return not bool(text)

print(regex("Testando a string para o exercicio"))
print(regex(' '))

'''
carlos = 'carlos'
for i in range(0, len(carlos)):
    print(carlos[i] * (i+1))
