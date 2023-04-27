populacaoNA = int(input("Digite a população de Nova Andradina: "))
fraseNA = (f"Nova Andradina tem a população de {populacaoNA}")

populacaoIV = int(input("Digite a população de Ivinhema: "))

popTotal = populacaoNA + populacaoIV

fraseTotal = (f"{fraseNA}, Ivinhema a população de {populacaoIV} e o total de {popTotal}")

print(fraseNA + "\n" + fraseTotal)