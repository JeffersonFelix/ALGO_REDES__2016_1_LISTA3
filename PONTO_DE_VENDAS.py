#Centro Universitário de João Pessoa - Unipê
#Curso: Redes de Computadores
#Disciplina: Algoritmo e Programação
#Professor: Jefferson Ferreira Barbosa
#Aluno: Jefferson Felix Gomes Matrícula: 1510010879
#Programa: PONTO DE VENDAS

valores_produtos = [float(input("Digite o primeiro valor: ")),
           float(input("Digite o segundo valor: ")),
           float(input("Digite o terceiro valor: ")),
           float(input("Digite o quarto valor: ")),
           float(input("Digite o quinto valor: "))]

inferior_50 = 0
entre50_e_80 = 0
acima_80 = 0

for valores in valores_produtos:
    if valores < 50:
        inferior_50 = inferior_50 + 1
    if (valores >= 50) and (valores <= 80):
        entre50_e_80 = entre50_e_80 + 1
    if valores > 80:
        acima_80 = acima_80 + 1

print("%d A quantidade de produtos com preço inferior a R$50,00" % inferior_50)
print("%d A quantidade de produtos com preço entre R$50,00 e R$80,00" % entre50_e_80)
print("%d A quantidade de produtos com preço acima R$80,00" % acima_80)
