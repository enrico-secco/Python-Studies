# ver se é triângulo

def Triangulo(lado1, lado2, lado3):
    if (lado3 < (lado1 + lado2)) & (lado2 < (lado1 + lado3)) & (lado1 < (lado2 + lado3)):
        print(" É um triângulo")

    else:
        print("não é um triângulo")



lado_um= int(input("digite o lado 1: "))

lado_dois= int(input("digite o numero 2: "))

lado_tres= int(input("digite o numero 3: "))

Triangulo(lado_um,lado_dois,lado_tres)