import os

def add_lista(lista):
        item = input("digite o que deseja adicionar na lista: ")
        lista.append(item)
        exibir_lista(lista)

def eliminar_lista(lista):
        item = input("Digite que item você deseja eliminar: ")
        if item in lista:
            lista.remove(item)
            exibir_lista(lista)

def exibir_lista(lista):
        print(lista)

def gravar_lista(lista):
    nome_arq = input("Digite um nome para seu arquivo: ")
    nome_arq += ".txt"
    with open (nome_arq,"w") as arquivo:
        for item in lista:
             arquivo.write(item + "\n")
    print("GRAVADO", {nome_arq})

def carregar_lista(lista):
    nome_arq = input("Digite o nome do arquivo que você deseja carregar: ")
    nome_arq += ".txt"
    try: 
        with open (nome_arq,"r") as arquivo:
            lista.clear()
            for linha in arquivo:
                lista.append(linha.strip())
        print("LISTA CARREGADA COM SUCESSO", {nome_arq})

    except FileNotFoundError:
        print("O arquivo não foi encontrado, tente novamente.")
    except Exception as e:
        print("Ocorreu um erro", e)

def ordenar_lista(lista):
    lista.sort(reverse = True)
    print("Lista ordenada com sucesso!")

def listar_arq(extensao= ".txt"):
    diretorio = os.getcwd()
    arquivos = os.listdir(diretorio)
    print(f"Os arquivos .{extensao} desse diretório são: ")
    for lista_arquivo in arquivos:
        if lista_arquivo.endswith(extensao):
            print(lista_arquivo)
    

def menu_principal():

    lista = []

    continuar = True

    while continuar:
        print ("Escolha uma das seguintes opções:")
        print ("1 - adicionar item da lista")
        print ("2 - eliminar item da lista")
        print ("3 - mostrar a lista")
        print ("4 - gravar lista")
        print ("5 - listar arquivos")
        print ("6 - carregar lista")
        print ("7 - ordenar lista")
        print ("8 - Sair")

        opcoes = (input("Sua escolha: "))

        if opcoes == "1":
            add_lista(lista)
        elif opcoes == "2":
            eliminar_lista(lista)
        elif opcoes == "3":
            exibir_lista(lista)
        elif opcoes == "4":
             gravar_lista(lista)
        elif opcoes == "5":
            listar_arq()
        elif opcoes == "6":
            carregar_lista(lista)
        elif opcoes == "7":
            ordenar_lista(lista)
        elif opcoes == "8":
            continuar = False
        else:
            print ("Dados inválidos, tente novamente.")

        print()
    
    print("Obrigado por utilizar nosso progama de listas!")
        
if __name__ == "__main__":
    menu_principal()