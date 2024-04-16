class Movie:
    platform = "OneBitFilmes"
    def __init__(self, name, yearLaunch, includedPlan, durationMinutes, avaliacao=None):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.totalEvaluation = 0
#        self.avaliacao = avaliacao
        self.durationMinutes = durationMinutes
        self.evaluators = 0
    
    def __str__(self):
        return f"Filme: {self.name}"
    
    def technical_sheet(self):
        # if self.note is None:
        #     self.set_note()
        # if self.notas is None:
        #     self.notas()
        print("*** Dados do Filme ***")
        print(f"Plataforma: {Movie.platform}")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Está no plano? {self.includedPlan}")
        print(f"Avaliação do filme: {self.totalEvaluation}")
        print(f"Duração do filme: {self.durationMinutes}")
        print(f"Total de avaliadores: {self.evaluators}")
#        print(f"Total de avaliações: {self.avaliacao}")

    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        print(f"Média do filme {self.name}: {self.totalEvaluation/self.evaluators}\n")

#    def set_note(self):
#        nota = float(input("Avaliação:\n"))
#        self.note = nota
    
    # def notas(self):
    #     avaliacoes = randint(1000, 3000)
    #     self.avaliacao = avaliacoes
        


mario = Movie("Super Mario Bros", 2023, False, 125)
mario.evaluate(9.5)
mario.evaluate(10.0)
mario.technical_sheet()
mario.average()

# Mudando a plataforma
Movie.platform = "Netflix"
avatar = Movie("Avatar", 2023, False, 180)
avatar.evaluate(8.5)
avatar.evaluate(9)
avatar.technical_sheet()
avatar.average()