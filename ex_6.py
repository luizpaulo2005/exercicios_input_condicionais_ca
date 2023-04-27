nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media_ponderada = (nota1 * 0.2 + nota2 * 0.3 + nota3 * 0.5)

if media_ponderada >= 6:
    resultado_final = "Aprovado"
else:
    resultado_final = "Reprovado"

print(f"{media_ponderada} - {resultado_final}")

# Exemplo 1

# Digite a primeira nota: 10
# Digite a segunda nota: 10
# Digite a terceira nota: 1
# 5.5 - Reprovado

# Exemplo 2

# Digite a primeira nota: 7
# Digite a segunda nota: 10
# Digite a terceira nota: 10
# 9.4 - Aprovado

# Exemplo 3

# Digite a primeira nota: 7
# Digite a segunda nota: 5
# Digite a terceira nota: 10
# 7.9 - Aprovado