# args
def sum(*num):
    num_total = 0
    for n in num:
        num_total += n
    print(f"A soma é: {num_total}")

sum(7)
sum(7, 9)
sum(7, 9, 10, 11)

# kwargs
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")

print("### Curso ###")
presentation(name="Python", category="Backend", level="Iniciante")
presentation(name="Visão Computacional com Python", category="IA", level="Avançado")
presentation(name="Dashboards com Dash", category="Data Science", level="Intermediário")
