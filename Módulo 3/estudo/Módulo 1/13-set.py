gamesSet = {"Fifa 23", "Red Dead 2", "Star Wars", "Zelda", "Mario",
            "Resident Evil 4"}

# não possibilita recuperar valores utilizando o fatiamento/slice

# 1 - tamanho do set
print(len(gamesSet))

# 2 - True e 1 são considerados o mesmo valor
exampleSet = {"Fifa 23", True, 1, 90.50}
print(exampleSet)

# 3 - adicionar item de outro set
gamesSet.update(exampleSet)
print(gamesSet)

# 4 - remover um item no set
gamesSet.remove(True)
gamesSet.remove(90.50)
print(gamesSet)
