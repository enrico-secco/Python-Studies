import random

print("Bem vindo")

num_aleatorio = random.randint(1,100)


nome = input("Digite seu nome: ")



print("numero gerado %d" % (num_aleatorio))


contador = 1;
#se o contador começasse com 0, a soma de contador teria que vir antes do print. E while < 7 e contador == 6
while contador <= 7 :
    num_entra = int(input("Digite o número: "))
    if num_aleatorio == num_entra:
        print("Você acertou com %d tentativas" % contador)
        contador = 7 # break ia travar o programa



    elif  num_entra < num_aleatorio :
        print(" Numero errado para menos, você tentou %d tentativas" % contador)
        contador = contador + 1


    else:
        print("Numero errado para mais, você tentou %d tentativas" % contador)
        contador = contador + 1


    if contador == 7:
        print("Última chance")


