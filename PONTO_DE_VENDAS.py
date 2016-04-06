# Centro Universitário de João Pessoa - Unipê
# Curso: Redes de Computadores
# Disciplina: Algoritmo e Programação
# Professor: Jefferson Ferreira Barbosa
# Aluno: Jefferson Felix Gomes Matrícula: 1510010879
# Programa: PONTO DE VENDAS

valores_produtos = list()

for i in range(1, 6):
    valores_produtos.append(float(input("Digite o preço do produto n. %d: " % i)))

inferior_50 = 0
entre50_e_80 = 0
acima_80 = 0
media = (float(valores_produtos[0]) + float(valores_produtos[1]) + float(valores_produtos[2]) + float(
    valores_produtos[3]) + float(valores_produtos[4])) / 5

for valores in valores_produtos:
    if valores < 50:
        inferior_50 = inferior_50 + 1
    if (valores >= 50) and (valores <= 80):
        entre50_e_80 = entre50_e_80 + 1
    if valores > 80:
        acima_80 = acima_80 + 1

print("(%d) a quantidade de produtos com preço inferior a R$50,00" % inferior_50)
print("(%d) a quantidade de produtos com preço entre R$50,00 e R$80,00" % entre50_e_80)
print("(%d) a quantidade de produtos com preço acima R$80,00" % acima_80)
print("A média de preço dos produtos R$: %.2f" % media)
