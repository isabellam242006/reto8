import numpy

def calcular_arctan(x,n):
  arctan = 0
  for i in range (n):
    arctan += ((-1) ** i)*((x ** (2 * i + 1))/(2* i + 1))
  return arctan

if __name__ == "__main__":
  x = float(input("Ingrese número entre -1 y 1 para x: "))
  n = 1
  if x>1 or x<-1:
    print("No es posible calcular el valor")
  else:
    while True:
      arctan = calcular_arctan(x,n)
      margen_error = abs((numpy.arctan(x) - arctan) / (numpy.arctan(x))) * 100
      n += 1
      if margen_error < 0.1:
        print("El valor de n debe ser " + str(n) + " para obtener un margen de error menor al 0.1%")
        break

print("El valor aproximado es " + str(arctan))
print("El valor real es " + str(numpy.arctan(x)))
print("El margen de error es de " + str(margen_error))