print("----------------------------")
print("O programa está em execução")
print("----------------------------")

nome = input("Digite seu nome: ")

materia = input('Digite a matéria: ')

nota1 =  float(input('Digite sua primeira nota: '))
nota2 =  float(input('Digite sua segunda nota: '))
nota3 =  float(input('Digite sua terceira nota: '))
nota4 = float(input('Digite sua quarta nota: '))



soma_notas = nota1 + nota2 + nota3 + nota4

média = soma_notas/4


if média < 7:
    print('Aluno %s ,você foi REPROVADO. Sua média em %s foi %.2f.' % (nome, materia, média))
    # %.2f. -> duas casas decimais depois da vírgula
else:
    print('PARABÉNS, aluno %s , você foi APROVADO. Sua média em %s foi %.2f.'
          % (nome, materia, média))


