# 1 - crie uma função que receba dois argumentos. O primeiro nome e o segundo
# nome
def full_name(fname, lname):
    print(f"Nome completo: {fname} {lname}")
    
full_name("Victor", "Rodrigues")

# 2 - crie uma função que some dois numeros

def sum(a, b):
    return a + b

print(sum(10, 50))

# 3 - argumentos default de uma função
def address(country="Brazil"):
    print(f"Eu moro no {country}")
    
address()
address("Canadá")

# 4 - avaliação do jogo
def rating_game(qtdRating):
    gameName = input("Nome do jogo:\n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo:\n"))
        sum += note
    print(f"Média de avaliação do jogo {gameName} é: {sum/qtdRating}")

rating = int(input("Digite quantas avaliações deseja fazer no jogo:\n"))
rating_game(rating)
