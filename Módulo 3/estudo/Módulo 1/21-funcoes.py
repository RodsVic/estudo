def welcome():
    return "Hello World"

welcome()

def sum():
    return 5 + 4

sum()

def create_game():
    name = input("Dgite o nome do jogo:\n")
    yearLaunch = int(input("Digite o ano de lançamento:\n"))
    gamePrice = float(input("Digite o preço do jogo:\n"))
    gameRating = float(input("Digite a nota de avaliação do jogo:\n"))
    
    print(f"{name} - R${gamePrice}")

create_game()
create_game()