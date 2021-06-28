#Espao somente de 15 caracteres

def truncar_texto(frase):
    if len(frase) > 15:
        return frase[:12] + "..."
        #retorna do 0:12  -> como é 15 o tamanho, colocou 12 pra adicionar os ... e dar 15
    else:
        return frase


print(truncar_texto("Pedro dormiu agora"))