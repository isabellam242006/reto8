n = int(input("Ingrese un número natural: "))
for i in range(1, n + 1):
  factorial = 1
  for p in range(1, i + 1):
    factorial *= p
  print(p,factorial,sep=",")