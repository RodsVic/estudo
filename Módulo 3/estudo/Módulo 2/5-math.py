import math

# 1 - Acessar o número pi
print(math.pi)
print(f"{math.pi:.2f}")

# 2 - Acessar o número de Euller
print(math.e)
print(f"{math.e:.2f}")

# 3 - Arredondando número para cima e para baixo
num1 = 10.4
print(math.ceil(num1))
print(math.floor(num1))

# 4 - Fatorial de um número
num2 = int(input("Digite um número para o fatorial\n"))
print(math.factorial(num2))

# 5 - Potência de um número
print(math.pow(5))

# 6 - Raiz quadrada de um número
print(math.sqrt(169))

# 7 - MDC
mdc = math.gcd(25, 100)
print(mdc)

# 8 - Logaritmo
print(math.log(10))
