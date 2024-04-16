'''
Classe Produto e método desconto
Desenvolva uma classe em Python para atender as seguintes especificidades 
de um Produto:
Cada produto deve ter um preço e um nome.
A classe deve ter um método construtor e o método dundle str.
A classe deve ter um método para desconto. O método deve receber o desconto 
em percentual e realizar o cálculo de quanto ficaria o preço final com o 
desconto.
'''

class Produto:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
            
    def __str__(self):
        return f"Produto: {self.name}: R${self.price:.2f}"
    
    def technical_sheet(self):
        print("*** Dados do Produto ***")
        print(f"Nome do produto: {self.name}")
        print(f"Preço do produto: {self.price}$")
    
    def desconto(self, perc):
        desc = (self.price / 100) * perc
        final = self.price - desc
        return f"Com {perc}% de desconto, o produto {self.name} custaria R${final:.2f}\n"

vassoura = Produto("Vassoura", 11)
vassoura.technical_sheet()
print(vassoura.desconto(10))

mop = Produto("Mop", 40)
mop.technical_sheet()
print(mop.desconto(10))
