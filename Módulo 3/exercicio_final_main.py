from exercicio_final import ContactBook

def main():
    agenda = ContactBook()

    while True:
        print("\nMenu:")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Remover contato")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            agenda.adicionar_contato()
        elif opcao == "2":
            agenda.listar_contatos()
        elif opcao == "3":
            agenda.buscar_contato()
        elif opcao == "4":
            agenda.remover_contato()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
