# reto8
1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

*Para este punto utilicé la función ```for i in range``` con el objetivo de escanear cada número dentro del rango de 1 a 100. Luego imprimo todos estos números y sus respectivos cuadrados separados por comas*

```python
for i in range(1,101):
  print(i, i**2, sep=",")
```
2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

*Para este punto realicé algo muy similar a lo anterior, solo que esta vez añadí que se escaneran los números de dos en dos con el fin de que solo mostrara los números pares. Además el primer rango va desde 1 a 999 y el segundo desde 2 hasta 1000.*

```python
for i in range(1,1000,2):
  print(i)

for i in range(2,1001,2):
  print(i)
```
3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

*Para este punto se añadió un ```for i in range``` de la siguiente forma: Inicia desde la i ingresada hasta 1 y desciende de a uno en uno(Por eso el -1) Además se añadió la condición de que solo mostrara los números que al dividir por 2 su residuo es 0, es decir que son pares.*

```python
i = int(input("ingrese un número mayor o igual que 2: "))
for i in range(i,1,-1):
  if i%2==0:
    print(i)
```
4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial

*Se crean dos rangos, uno para escanear todos los números hasta el número dado y otro para calcular el factorial de dichos números. En este caso p es el número escaneado, factorial es la multiplicación consecutiva de todos los números desde 1 hasta ese número dado, y así con todos los p en ese rango). En resumen se utilizó ```for in range``` de forma anidada*
```python
n = int(input("Ingrese un número natural: "))
for i in range(1, n + 1):
  factorial = 1
  for p in range(1, i + 1):
    factorial *= p
  print(p,factorial,sep=",")
```
5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.

*Para este punto se estableció un rango desde 1 hasta una potencia dada y luego se hizo una multiplicación consecutiva de 2 hasta completar dicho rango*
```python
n=int(input("Ingrese la potencia: "))
potencia=1

for i in range(1, n+1):
  potencia *=2

print("2 a la potencia de " + str(n) + " es " + str(potencia))
```
6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**)

*Para este punto se hizo algo similar que el anterior, solo que en este caso se estableció potencia como uno y esta se multiplicará por x consecutivamente hasta llegar a un número n dado*
```python
x = int(input("Ingrese un número: "))
n = int(input("Ingrese el número de la potencia: "))
potencia = 1

for i in range(n):
  potencia *=x
    
print(str(x) + " elevado a la potencia de " + str(n) + " es " + str(potencia))
```
7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9

*Para este punto se establecieron dos rangos. Para hacer las tablas de 1 hasta 9, se multiplica cada valor del primer rango con el del segundo*

```python
for i in range(1, 10):
  print("La tabla del " + str(i) + " es: \n")
  for n in range(1, 11):
    multiplicacion = i * n
    print(str(i) + " X " + str(n) + " = " + str(multiplicacion) + "\n")
```
*Para los siguientes puntos se usó una estructura similar:*

- Primero se definió la función factorial en los puntos en los que se requirió
- Luego se definió la función para calcular el valor aproximado, en esta se establece un rango desde 1 hasta n, sabemos que n es en realidad el número de términos (Es decir el número de veces que queremos que se aplique la fórmula) Para este tipo de series entre más términos se utilicen, más cerca al valor real se está llegando.
- Luego de esto se declaran las variables
- Por último se realiza un bucle ```while``` para comparar los resultados del valor aproximado y el valor real(Calculandolo con las funciones arctan, sin y exp). En este bucle se inicia con el valor n=0 se va iterando hasta que se llegue a una diferencia muy mínima entre ambos valores (Un margen de error menor a 0.1%) Luego se cierra el bucle con un ```break``` y se imprimen los resultados.

8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación

```python
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
```
9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
```python
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
```
10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
```python
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
```







