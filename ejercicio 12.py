from math import sqrt

def calculo_cuadrados_perfectos(n):
  s = []
  t = []
  for i in range (n+1):
    t.append(i)
  for q in t:
    if sqrt(q) in t:
      s.append(q)
    print(.format(n))
  for x in s:
    print(x)

if __name__== '__main__'
  n = int(input("Introduce un numero entero: "))
  calculo_cuadrados_perfectos(n)