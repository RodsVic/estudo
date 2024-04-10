# 1 - fatorial de um numero
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))

numero = int(input("Digite um numero para o fatorial:\n"))
print(f"O fatorial de {numero} é: {factorial(numero)}")

# 2 - soma total de um numero
def total_sum(num):
    if num == 1:
        return 1
    else:
        return (num + total_sum(num - 1))

number = int(input("Digite um numero para a soma:\n"))
print(f"A soma total do {number} é: {total_sum(number)}")
