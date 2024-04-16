'''
## Advinhe o Número

Escreva um programa em Python que gera um número aleatório para que o 
usuário tente acertar o número. Algumas sugestões para o programa:

1. Utilizar um laço de repetição para que o programa execute até que o 
usuário informe um número referente a opção para sair do programa.
2. Utilizar o módulo random para gerar valores aleatórios dentro de um 
intervalo. Ex: 1 a 10.
3. Lê o número que o usuário digitar via input e comparar se é o mesmo 
número que o programa sorteou.
'''
from random import randint

num = randint(1, 10)

while True:
    inp = int(input("Adivinhe o número:\n"))
    if inp == num:
        print("Parabéns! Você acertou!")
        break
    elif inp == 999:
        break
    else:
        print("Númerro errado!")
        print("Tente novamente\n")
        