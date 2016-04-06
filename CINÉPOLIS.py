#Centro Universitário de João Pessoa - Unipê
#Curso: Redes de Computadores
#Disciplina: Algoritmo e Programação
#Professor: Jefferson Ferreira Barbosa
#Aluno: Jefferson Felix Gomes Matrícula: 1510010879
#Programa: PONTO DE VENDAS

questionario = list()

for i in range(0, 5):
    questionario.append(int(input("Avalie os Filmes: 1 REGULAR, 2 BOM, 3 ÓTIMO: ")))

regular_1 = 0
bom_2 = 0
otimo_3 = 0

for resultado in questionario:
    if resultado == 1:
        regular_1 = regular_1 + 1
    if resultado == 2:
        bom_2  = bom_2 + 1
    if resultado == 3:
        otimo_3 = otimo_3 + 1

print("A quantidade de pessoas que responderam: REGULAR (%d)" % regular_1)
print("A quantidade de pessoas que responderam: BOM (%d)" % bom_2)
print("A quantidade de pessoas que responderam: ÓTIMO (%d) " % otimo_3)
