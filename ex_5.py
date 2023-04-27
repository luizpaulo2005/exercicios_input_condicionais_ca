number = int(input("Enter a number: "))

if (number > 0):
  if (number % 2 == 0):
    print("A")
  else:
    print("B")
  print("C")
print("D")

if (number > 0):
  if (number % 2 == 0):
    print("E")
  print("F")
else:
  print("G")
print("H")

# Quais são as letras mostradas no console quando o programa acima é executado e a variável number tem o valor de 5?
# B C D F H

# Quais são as letras mostradas no console quando o programa acima é executado e a variável number tem o valor de 6?
# A C D E F H

# Quais são as letras mostradas no console quando o programa acima é executado e a variável number tem o valor de -5?
# D G H

# Quais são as letras mostradas no console quando o programa acima é executado e a variável number tem o valor de -6?
# D G H