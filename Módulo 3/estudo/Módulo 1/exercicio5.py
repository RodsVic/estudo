'''
Exercicio 5:
*Conta letras maiúsculas e minúsculas:
-> Escreva uma função Python que receba uma string e conte o número de letras
maiúsculas e minúsculas desta string
def contador():
    c1 = 0
    c2 = 0
    string = str(input("Digite a string:\n"))
    for i in list(string):
        if i.islower():
            c1 += 1
        elif i.isupper():
            c2 += 1
        else:
            continue
    print(f"Maiúsculas = {c2}\nMinúsculas = {c1}")
contador()
'''

'''
*Lista de números pares e ímpares:
-> Escreva uma função Python para imprimir os números pares e ímpares em duas
listas separadas para cada uma
def separador():
    par = []
    impar = []
    
    while True:
        num = int(input("Digite um numero:\n"))
        if num == 000:
            break
        elif num % 2 == 0:
            par.append(num)
        elif num % 2 != 0:
            impar.append(num)
    print(par, impar)
separador()
'''