'''
## Agenda de Contatos

Desenvolva uma agenda de contatos persistindo as informações em arquivo. O programa deve 
seguir as especificidades:

1. Criar o arquivo Agenda contendo quatro métodos:
    1. Um método para adicionar contato.
    2. Um método para listar contatos.
    3. Um método para remover contatos.
2. Criar um arquivo principal para a aplicação que importar o módulo de agenda e chamar cada 
um dos métodos desenvolvidos de acordo com a opção escolhida.
'''
from contato import Contact
from contato_agenda import ContactBook

contact_book = ContactBook()

while True:
    print("\n--- Opções Agenda de Contatos ---")
    print("1. Adicionar Contato")
    print("2. Remover Contato")
    print("3. Listar Contatos")
    print("4. Buscar Contato")
    print("5. Sair")

    choice = input("Escolha a opção: ")

    if choice == "1":
        name = input("Informe o nome: ")
        phone = input("Informe o telefone: ")
        email = input("Informe o e-mail: ")
        contact = Contact(name, phone, email)
        contact_book.add_contact(contact)
        print("Contato adicionado com sucesso.")
    elif choice == "2":
        name = input("Informe o nome para remover: ")
        contact_book.remove_contact(name)
        print("Contato removido com sucesso\n.")
    elif choice == "3":
        contact_book.display_contacts()
    elif choice == "4":
        name = input("Procure por um nome: ")
        contact_book.search_contact(name)
    elif choice == "5":
        print("Saindo do programa.")
        break
    else:
        print("Opção Inválida. Utilize uma opção de 1 a 5\n")