def add_lista(lista):
        item = input("digite o que deseja adicionar na lisa: ")
        lista.append(item)
        exibir_lista(lista)

def eliminar_lista(lista):
        item = input("Digite que item você deseja eliminar: ")
        if item in lista:
            lista.remove(item)
            exibir_lista(lista)

def exibir_lista(lista):
        print(lista)

def menu_principal():

    lista = []

    continuar = True

    while continuar:
        print ("Escolha uma das seguintes opções:")
        print ("1 - adicionar item da lista")
        print ("2 - eliminar item da lista")
        print ("3 - mostrar a lista")
        print ("4 - Sair")

        opcoes = (input("Sua escolha: "))

        if opcoes == "1":
            add_lista(lista)
        elif opcoes == "2":
            eliminar_lista(lista)
        elif opcoes == "3":
            exibir_lista(lista)
        elif opcoes == "4":
            continuar = False
        else:
            print ("Dados inválidos, tente novamente.")

        print()
    
    print("Obrigado por utilizar nosso progama de listas!")
        
if __name__ == "__main__":
    menu_principal()