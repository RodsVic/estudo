gamesList = ["Resident Evil 4", "Star Wars", "Legend of Zelda",
             "Red Dead 2", "Mario Odyssey", "Luigis Mansion 3"]

#tamanho da lista
print(len(gamesList))

#retornar item pelo indice
print(gamesList.index("Mario Odyssey"))

#adicionar item ao final da lista
gamesList.append("GTA V")

#ordenar lista
gamesList.sort()

#copiar os itens de uma lista para outra
gamesList2 = gamesList.copy()
gamesList2.remove("Star Wars")

#remover os itens da lista
# gamesList.clear()

print(gamesList)
print(gamesList2)
