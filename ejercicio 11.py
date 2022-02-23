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