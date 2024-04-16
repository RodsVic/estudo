'''
*Contagem Regresiva:
-> Faça um programa para escrever a contagem regressiva de um foguete.
O programa deve imprimir 10, 9, 8, ..., 1, 0 e disparar um "beep"
import winsound
for i in range(10,0,-1):
    print(i)
print("Lançar")
winsound.Beep(2500, 500)
'''

'''
*Tabuada
-> Faça um programa que calcule a tabuada de um número, com valores iniciais
e finais informados pelo usuário
num = int(input("Digite o numero\n"))
for i in range(11):
    print(f"{num} x {i} = {num*i}")
'''
