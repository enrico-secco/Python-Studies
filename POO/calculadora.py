
class Calculadora:

    def __init__(self, a,b):
        self.a = a
        self.b = b


    def soma(self):
       resultado = self.a + self.b
       self.impressao(resultado) #chama a função impressao dentro da função soma. Substitui o parâmetro do a por resultado

    def subtracao(self):
        resultado =  self.a - self.b
        self.impressao(resultado)

    def impressao(self):
        print(a)