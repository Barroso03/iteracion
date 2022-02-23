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