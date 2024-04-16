'''
## Lendo n linhas de um arquivo

Escreva um programa Python para ler as primeiras n linhas de um arquivo.

1. O nome do arquivo e a quantidade de linhas devem ser passadas via 
parâmetro na função.
'''
def leitura(arquivo, linhas):
    c = 0
    with open(arquivo, "r", encoding="utf-8") as file:
        while c < linhas:
            linha = file.readline()
            print(linha.rstrip())
            c += 1

leitura("dados/names.txt", 3)
leitura("dados/names.txt", 10)
leitura("dados/names.txt", 8)


'''
Alternativa 2 - Código do professor

def file_read_from_line(fname, nlines):
    from itertools import islice
    with open(fname, encoding="utf-8") as file:
        for line in islice(file, nlines):
            print(line)

file_read_from_line("dados/names.txt", 2)
'''
