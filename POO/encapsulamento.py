class Livro:

    def __init__(self,titulo, autor):
        self.__titulo = titulo  #__ faz ela ser privada
        self.autor = autor


    @property # para get, pegar informações do atributo
    def titulo(self):
        return self.__titulo


    @titulo.setter # método título tem função de inserir na variável título
    def titulo(self,titulo):
        self.__titulo = titulo


livro1 = Livro("curso", "joao")
print(livro1.autor)
print(livro1.titulo) #nome da função titulo

livro1.titulo = "novo autor"
print(livro1.titulo)
