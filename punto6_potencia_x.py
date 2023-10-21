x = int(input("Ingrese un número: "))
n = int(input("Ingrese el número de la potencia: "))
potencia = 1

for i in range(n):
  potencia *=x
    
print(str(x) + " elevado a la potencia de " + str(n) + " es " + str(potencia))