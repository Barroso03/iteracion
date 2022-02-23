# iteracion

La direeción de nuestro repositorio es:(https://github.com/Barroso03/iteracion.git)

La dirección del replit es:(https://replit.com/@Barroso03/iteracion-4#.replit)

## Ejercicio 6

```

```
***
## Ejercicio 7

```
def encuentra_potencia(numero, base):
    
    factor = 1
    while factor <= numero:
        factor *= base
    return factor//base


def imprime_digito_en_base(digito):
  if digito < 10:
    
    print("{:d}".format(digito), end="")
  else:
    
    digito_transformado = chr(digito - 10 + ord('A'))
    
    print("{}".format(digito_transformado), end="")

def imprime_en_otra_base(numero, base):
  
    factor = encuentra_potencia(numero, base)
    while True:
        digito = numero // factor
      #Vamos imprimiendo los digitos uno por uno
        imprime_digito_en_base(digito)
        numero %= factor
        factor = factor//base;
        if factor == 0:
            break 

def flujo_programa():
  numero = int(input("Introduzca un numero entero: "))
  while True:
    base = int(input("Introduzca la base: "))
    if base >= 2:
      
      imprime_en_otra_base(numero, base)
      break
    else:
      print("Debe ingresar una base entre 2 y 36")

if __name__ == "__main__":

  flujo_programa()
```
***
## Ejercicio 8

```
import tabulate

def descomponer():

  separador = str(input("Introduce el separador que desea utilizar: "))
  cadena = str(input("Introduce un texto para analizar: "))

  ca = cadena.split(separador)
  
  lista = []
  for i in range(0, len(ca)):
    lista.append(list(ca[i:i+1]))

  table = lista
  headers = ["nº", "Cadena"]
  print(tabulate.tabulate(table, headers, tablefmt = "fancy_grid", showindex = True))
```
***
## Ejercicio 9

```
import tabulate

diccionario =  ["Patata", "Fotos", "Ancla",                             "Cucaracha"]

def palabra(dicccionario):

  palabra = []

  for i in range(0, len(diccionario)):
    diccionario.sort()
    z = [i + 1, diccionario[i], i, i + 2]
    palabra.append(z)
  
  tabla = palabra

  headers = ["i", "diccionario", "anterior", "siguiente"]

  print("Este es el diccionario:")
  print(tabulate.tabulate(tabla, headers, tablefmt = "fancy_grid"))


def añadir():

  n = str(input("Introduce la palabra que quieres añadir al diccionario: "))
  diccionario.append(n)

  palabra(diccionario)
  
def delete():
  n = str(input("Introduce la palabra que quieres quitar del diccionario: "))
  diccionario.remove(n)

  palabra(diccionario)
  
def inicio():
  palabra(diccionario)
  añadir()
  delete()
```
***
## Ejercicio 10

```

```
***
## Ejercicio 11

```
`Punto 1´
def mcd_euclides(x,y):
  while y != 0:
    xux = y
    y = x%y
    x = xux
  return x


`Punto 2´
def mcd_sumas_y_restas(x,y):
  while y != 0:
    xux = y
    y -= xux
    x = xux
  return x

#Creamos una función para iniciar ambos pasos

def inicio():

  1numero = 2
  2numero = 3
  print("punto 1",(mcd_euclides(x, y)))
  print("punto 2",(mcd_sumas_y_restas(x, y)))
```
***
## Ejercicio 12

```
from math import sqrt

def calculo_cuadrados_perfectos(n):
  s = []
  t = []
  for i in range (n+1):
    t.append(i)
  for q in t:
    if sqrt(q) in t:
      s.append(q)
    print( .format(n))
  for x in s:
    print(x)

if __name__== '__main__'
  n = int(input("Introduce un numero entero: "))
  calculo_cuadrados_perfectos(n)
```
***
