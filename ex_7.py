salario = float(input("Digite o salário: R$"))
id_cargo = int(input("Digite o código do cargo: "))
cargo = ""

salario_aumentado = 0

if id_cargo == 101:
    cargo = "Gerente"
    salario_aumentado = salario * 1.1
elif id_cargo == 102:
    cargo = "Engenheiro"
    salario_aumentado = salario * 1.2
elif id_cargo == 103:
    cargo = "Técnico"
    salario_aumentado = salario * 1.3
else:
    cargo = "Outro Cargo"
    salario_aumentado = salario * 1.4


diferenca_salario = salario_aumentado - salario

print(f"O cargo é {cargo}")
print(f"O salário é de R${salario:.2f}")
print(f"O salário com aumento é de R${salario_aumentado:.2f}")
print(f"A diferença salarial é de R${diferenca_salario:.2f}")

# Exemplo 1

# O cargo é Engenheiro
# O salário é de R$1000.00
# O salário com aumento é de R$1200.00
# A diferença salarial é de R$200.00

# Exemplo 2

# O cargo é Técnico
# O salário é de R$2790.00
# O salário com aumento é de R$3627.00
# A diferença salarial é de R$837.00

# Exemplo 3

# O cargo é Outro Cargo
# O salário é de R$5000.00
# O salário com aumento é de R$7000.00
# A diferença salarial é de R$2000.00