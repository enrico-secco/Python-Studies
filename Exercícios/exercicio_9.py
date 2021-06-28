#Calculadora interativa



def soma():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o número 2: "))

    return num1 + num2

def subtracao():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o número 2: "))

    return num1 - num2

def multiplica():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o número 2: "))

    return num1*num2

def divisao():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o número 2: "))

    return num1/num2

def menu():
    print("Selecione uma opção")
    print("1 - soma")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    opcao = int(input("Digite o número da opção"))

    if opcao == 1:
        soma()

    elif opcao == 2:
        subtracao()

    elif opcao == 3:
        multiplica()

    elif opcao == 4:
        divisao()

    else:
        print("Entrada inválida")


menu()
