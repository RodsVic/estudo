name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo\n"))
classification = float(input("Digite a nota de classificação do jogo\n"))

if classification > 8:
    print(f"O jogo {name} é muito bom")
else:
    print(f"O jogo {name} ainda não atingiu uma boa nota.")
    