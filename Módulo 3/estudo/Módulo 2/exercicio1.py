from strings import *
'''
## Módulo de strings

Escreva um módulo em python para tratar algumas strings e que possua as seguintes funcionalidades:

1. Inverter uma string de trás pra frente.
2. Retornar apenas letras com índice par.
3. Retornar apenas letras com índice ímpar.
'''
'''
reverse = lambda s: s[::-1]
pair = lambda s: s[0:len(s):2]
odd = lambda s: s[1: len(s): 2]
'''

print(inverse("Victor"))
print(even_string("Victor"))
print(odd_string("Victor"))
