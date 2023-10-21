n=int(input("Ingrese la potencia: "))
potencia=1

for i in range(1, n+1):
  potencia *=2

print("2 a la potencia de " + str(n) + " es " + str(potencia))