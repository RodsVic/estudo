listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

gameList = ["Mario Odyssey", "DK Country", "Luigis Mansion", "Kirby"]

newList = [x for x in gameList if "a" in x]
print(newList)

gamesFinished = [x for x in gameList if x != "Kirby"]
print(gamesFinished)
