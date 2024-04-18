num1 = int(input("Digite um número: "))

num2 = int(input("Digite outro número: "))

operacao = input("Digite que operação deseja fazer: +, -, *, /: ")


def sum(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mult(num1, num2):
    return num1 * num2
def div(num1, num2):
    if num2 == 0:
        return "0 não é um numero que pode ser dividido"
    else:
        return num1 / num2

if (operacao == "+"):
    print("O resultado é:")
    print(sum(num1, num2))
elif (operacao == "-"):
    print("O resultado é:")
    print(sub(num1, num2))
elif (operacao == "*"):
    print("O resultado é:")
    print(mult(num1, num2))
elif (operacao == "/"):
    print("O resultado é:")
    print(div(num1, num2))
else:
    print("Tente novamente, algo deu errado!")
