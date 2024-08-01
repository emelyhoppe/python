myList = []

while True:
    options = input(
        '''
        Escolha uma opção
        N: Novo número;
        S: Soma;
        Q: Sair;
        '''
    )

    if options == 'n':
        numero = int(input("Digite o número"))
        myList.append(numero)

    elif options == 's':
        print(sum(myList))

    elif options == 'q':
        break

    def sum(list):
        result = 0
        for i in list:
             result = result + i
        return result

