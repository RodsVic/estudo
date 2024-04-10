# 1 - função de potência de número
power = lambda num: num ** 2

# 2 - função que verifica se o numero é par
pair = lambda x: x % 2 == 0

# 3 - função que divide um numero por outro
divnum = lambda x, y: x / y

# 4 -  função que inverte uma string
reverse = lambda s: s[::-1]

print(power(5))
print(power(6))
print(pair(27))
print(pair(30))
print(divnum(10, 2))
print(divnum(10, 5))
print(reverse("Victor"))
print(reverse("Carlos"))
