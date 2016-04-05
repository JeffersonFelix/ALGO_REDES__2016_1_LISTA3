questionario = [int(input("Avalie os Filmes: 1 REGULAR, 2 BOM, 3 ÓTIMO: ")),
                int(input("Avalie os Filmes: 1 REGULAR, 2 BOM, 3 ÓTIMO: ")),
                int(input("Avalie os Filmes: 1 REGULAR, 2 BOM, 3 ÓTIMO: ")),
                int(input("Avalie os Filmes: 1 REGULAR, 2 BOM, 3 ÓTIMO: ")),
                int(input("Avalie os Filmes: 1 REGULAR, 2 BOM, 3 ÓTIMO: "))]
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

print("A quantidade de pessoas que responderam: REGULAR %d" % regular_1)
print("A quantidade de pessoas que responderam: BOM %d" % bom_2)
print("A quantidade de pessoas que responderam: ÓTIMO %d " % otimo_3)
