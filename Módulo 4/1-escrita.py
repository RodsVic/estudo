'''
*** Arquivos ***

1 - Opção w - write
2 - Opção a - append
3 - Opção r - read
'''

name = input("Digite seu nome:\n")

# Alternativa 1
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# Alternativa 2
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
