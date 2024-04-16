class Movie:
    name = ""
    yearLaunch = 0
    includedPlan = False
    note = 0
    durationMinutes = 0
    
# Primeiro filme
movie = Movie()
movie.name = "Super Mario Bros"
movie.yearLaunch = 2023
movie.includedPlan = False
movie.note = 5.0
movie.durationMinutes = 130
print("### Dados do Filme ###")
print(f"Nome do filme: {movie.name}\nAno de Lançamento: {movie.yearLaunch}")

# Segundo filme (TVShow)

got = Movie()
got.name = "Game of Thrones"
got.yearLaunch = 2011
got.includedPlan = False
got.note = 10.0
print("*** Dados da Série ***")
print(f"Nome da série: {got.name}\n"
      f"Ano de Lançamento: {got.yearLaunch}\n"
      f"Classificação da série: {got.note}")
