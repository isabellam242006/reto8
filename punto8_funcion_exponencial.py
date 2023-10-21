import math

def factorial(i):  #Definimos función factorial
  factorial = 1
  while i >1:
    factorial*=i
    i-=1
  return factorial

def calcular_exponencial(x,n):  
  exponencial=0
  for i in range (n+1):
    exponencial+=(x**i)/factorial(i)  
  return exponencial

if __name__ == "__main__":
  x = float(input("Ingrese número real para x: ")) 
  n = 1   

while True:
  exponencial = calcular_exponencial(x,n)
  margen_error = abs((math.exp(x) - exponencial) / (math.exp(x))) * 100   
  n += 1
  if margen_error < 0.1:
    print("El valor de n debe ser " + str(n) + " para obtener un margen de error menor al 0.1%")
    break

print("El valor aproximado es " + str(exponencial))
print("El valor real es " + str(math.exp(x)))
print("El margen de error es de " + str(margen_error))