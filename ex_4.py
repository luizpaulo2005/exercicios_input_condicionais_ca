prim = 20
sec = 10

if (prim < sec):
  prim = prim / 2
if (prim < 2 * sec):
  prim = prim * 2
  sec = sec / 2
else:
  prim = prim + 1
  sec = sec - 1

elasSaoIguais = (prim == sec)

if (elasSaoIguais):
  prim = prim + 1

print(prim, sec)

# Pense neste código em execução. Responda às perguntas abaixo:

# Quantas vezes, no total, o computador executa uma expressão condicional (de qualquer if)?
# 3

# Quantas vezes, no total, a expressão de um comando condicional if é avaliada para True?
# 0

# O if do meio possui um else. Quantas vezes o bloco da falsidade é executado?
# 1

# O que a última linha de código imprime no console?
# 21 9