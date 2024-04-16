gameFifa = {
    "name" : "Fifa 23",
    "yearLaunch" : 2022,
    "gamePrice" : 90.50,
    "classification" : 8.5,
    "genre" : ["esporte", "familia"]
    }

print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# 1 - recuperar um elemento do dicionário
print(gameFifa['genre'])
print(gameFifa.get('classification'))

# 2 - buscar apenas as chaves do dicionario
print(gameFifa.keys())

# 3 - buscar apenas os valores do dicionario
print(gameFifa.values())

# 4 - buscar itens do dicionario com chave e valor
print(gameFifa.items())

# 5 - adicionar itens no dicionario
gameFifa["players"] = 2
print(gameFifa)

# 6 - atualizar itens no dicionario
gameFifa.update({"players" : 1})
print(gameFifa)

# 7 - remover item no dicionario
gameFifa.pop("players")
print(gameFifa)
