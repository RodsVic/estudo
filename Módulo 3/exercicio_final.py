'''
## Agenda de Contatos

Desenvolva uma agenda de contatos utilizando Programação Orientada a Objetos.
 O programa deve seguir as especificidades:

1. Ter uma classe Contact contendo os atributos: name, phone e email
2. Ter uma classe ContactBook contendo quatro métodos:
    1. Um método para adicionar contato.
    2. Um método para listar contatos.
    3. Um método para buscar contatos.
    4. Um método para remover contatos.
3. Criar um arquivo principal para a aplicação que deve instanciar as duas 
classes criadas anteriormente e desenvolver e chamar cada um dos métodos 
desenvolvidos de acordo com a opção escolhida.
'''
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f"Nome: {self.name} \nTelefone: {self.phone} \nEmail: {self.email}"
    
class ContactBook:
    def __init__(self):
        self.contacts = {}
        
    def adicionar_contato(self):
        print("Informações do contato a ser adicionado:")
        
        self.name = input("Digite o nome do contato:\n")
        self.phone = input("Digite o número do contato:\n")
        self.email = input("Digite o email do contato:\n")
        
        self.contacts[self.name] = {'name': self.name, 'phone': self.phone, 'email': self.email}
        print(f"Contato {self.name} adicionado!\n")
    
    def listar_contatos(self):
        print("\nContatos na lista:")
        for i, contato in enumerate(self.contacts.values()):
            print(f"{i+1}. {contato['name']}")
    
    def remover_contato(self):
        name = str(input("\nInforme o nome do contato que deseja remover:\n"))
        if name in self.contacts:
            self.name = list(self.contacts.keys())
            del self.contacts[name]
            print("Contato removido\n")
        else:
            print("Nome de contato inválido\n")
    
    def buscar_contato(self):
        name = str(input("\nInforme o nome do contato que deseja buscar:\n"))
        if name in self.contacts:
            contato = self.contacts[name]
            print("\nInformaçoes do contato:")
            print("Nome:", contato["name"])
            print("Telefone:", contato["phone"])
            print("Email:", contato["email"])
        else:
            print("Contato não encontrado")
        
# agenda = ContactBook()
# agenda.adicionar_contato()
# agenda.listar_contatos()
# agenda.remover_contato()
# agenda.listar_contatos()
# agenda.buscar_contato()
