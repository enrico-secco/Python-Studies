# Calcular preço total da conta
# Maçã -> até 5kg 1,80 e 1,50 acima de 5kg
# Morango -> até 5k 2,50 e 2,20 acima de 5kg
# Preço -> acima de 8kg no total ou mais de 25 reais, ganha desconto de 10%

def calcula_valor(kg_morango, kg_maca):
    kg_morango = int(input("Quilo(s) de morango: "))
    kg_maca = int(input("Quilo(s) de maçã: "))

    if kg_morango >= 5:
        preco_morango = kg_morango * 2,20

    else:
        preco_morango = kg_morango * 2,50


    if kg_maca >= 5:
        preco_maca = kg_maca * 1,50

    else:
        preco_maca = kg_maca * 1,80



    kg_total = kg_maca + kg_morango
    preco_total = preco_morango + preco_maca

    if  kg_total > 8 or preco_total > 25 : # gerou tupla
        preco_total = (preco_total * 0,9)


    print("O valor total é %f" % (preco_total))

