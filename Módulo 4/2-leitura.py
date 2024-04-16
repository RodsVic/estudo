'''
*** Arquivos ***

1 - Opção w - write
2 - Opção a - append
3 - Opção r - read
'''

with open("dados/names.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(f"{line.rstrip()}")
