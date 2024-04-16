gamesList = ["Fifa", "God of War", "Red Dead 2", "Uncharted", 90.50]

# 1 - Iterando valores em uma lista
for game in gamesList:
    print(game)

# 2 - Quando a condição for atendida, o loop será encerrado
for game in gamesList:
    if game == "Red Dead 2":
        break
    print(game)

# 3 - Quando a condição for atendida, o loop vai para a próxima iteração
for game in gamesList:
    if game == "Read Dead 2":
        continue
    print(game)

# 4 - Avaliação do jogo
gameName = input("Nome do jogo:\n")
gameRating = int(input("Quantas avaliações você deseja fazer?\n"))

sum = 0
for i in range(gameRating):
    note = float(input("Digite a nota para o jogo:\n"))
    sum += note
print(f"Média de avaliação do jogo {gameName} é {sum/gameRating:.2f}")
