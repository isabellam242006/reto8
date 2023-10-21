import math

def factorial(i):
  factorial = 1
  while i >1:
    factorial*=i
    i-=1
  return factorial

def calcular_sin(x,n):
  sin=0
  for i in range (n+1):
    sin+= ((-1) ** i)*((x ** (2 * i + 1)) / factorial(2 * i + 1))
  return sin

if __name__ == "__main__":
  x = float(input("Ingrese número real para x: "))
  n = 1

while True:
  sin = calcular_sin(x,n)
  margen_error = abs((math.sin(x) - sin) / (math.sin(x))) * 100
  n += 1
  if margen_error < 0.1:
    print("El valor de n debe ser " + str(n) + " para obtener un margen de error menor al 0.1%")
    break

print("El valor aproximado es " + str(sin))
print("El valor real es " + str(math.sin(x)))
print("El margen de error es de " + str(margen_error))