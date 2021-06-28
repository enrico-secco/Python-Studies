#Colocar nome em maíusculo, com exceção de e da

def formatar_nome(nome_completo):
    nome_formatado = [nome.capitalize() for nome in nome_completo.split()]
    # split() -> quebrar a string em uma lista
    resultado = ' '.join(nome_formatado)
    # vai pegar uma lista e transformar em String "juntar".
    resultado = resultado.replace(' Da ',' da ').replace(' De ', ' de ')
    return resultado

print(formatar_nome("enrico secco"))







