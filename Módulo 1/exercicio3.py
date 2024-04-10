'''
Exercício 3:
*** Cálculo da Distância ***
-> Escreva um programa que pergunte a distância que um passageiro deseja
percorrer em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens
de até 200 km, e R$0,35 para viagens mais longas.
Preço da passagem = R$50,00
passagem = 50
distancia = int(input("Distância em km:\n"))

if distancia <= 200:
    preco = (distancia * 0.5) + passagem
elif distancia > 200:
    preco = (distancia * 0.35) + passagem

print(f"O valor da viagem será de {preco:.2f}, por {distancia}km a percorrer.")
'''

'''
*** Aumento de Salário do Funcionário ***
-> Escreva um programa que pergunte o salário do funcionário e calcule
o valor do aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para salários inferiores ou iguais a R$1250,00, o aumento será de 15%.

'''
salario = float(input("Salário do funcionário:\n"))

if salario > 1250:
    salario_novo = (salario * 10 / 100) + salario
elif salario <= 1250:
    salario_novo = (salario * 15 / 100) + salario

print(f"O salário novo será de {salario_novo:.2f}")