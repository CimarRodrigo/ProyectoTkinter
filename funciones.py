def negacion(cadena):
  p = True
  cadena = "p \t\t -p" + "\n" + str(p) + "\t\t" + str(not(p))
  return cadena

def conjuncion(cadena):
  p = True
  q = True
  c = 0
  cont = 0
  cadena = "p \t\t q \t\t p∧q" + "\n"
  while cont != 4:
    if p == True and q == True:
      res = True
    else:
      res = False
    cadena += str(p) + "\t\t" + str(q) + "\t\t" + str(res) + "\n"
    
    c += 1
    if c == 2:
      p = not(p)
    q = not(q)
    cont += 1
  return cadena
def disyuncion(cadena):
  p = True
  q = True
  c = 0
  cont = 0
  cadena = "p \t\t q \t\t p∨q" + "\n"
  while cont != 4:
    if p == False and q==False:
      res = False
    else:
      res = True
    
    cadena += str(p) + "\t\t" + str(q) + "\t\t" + str(res) + "\n"
    c += 1
    if c == 2:
      p = not(p)
    q = not(q)
    cont += 1
  return cadena
def disyuncion_exclusiva(cadena):
  p = True
  q = True
  c = 0 
  cont = 0
  cadena = "p \t\t q \t\t p⊻q" + "\n"
  while cont != 4:
    if p != q :
      res = True
    else:
      res = False

    cadena += str(p) + "\t\t" + str(q) + "\t\t" + str(res) + "\n"
    c += 1
    if c == 2:
      p = not(p)
    q = not(q)
    cont += 1
  return cadena
def condicional(cadena):
  p = True
  q = True
  c = 0
  cont=0
  cadena = "p \t\t q \t\t p->q" + "\n"
  while cont != 4:
    if p == True and q == False:
      res = False
    else:
      res = True
    cadena += str(p) + "\t\t" + str(q) + "\t\t" + str(res) + "\n"
    c += 1
    if c == 2:
      p = not(p)
    q = not(q)
    cont += 1
  return cadena

def bicondicional(cadena):
  p = True
  q = True
  c = 0
  cont = 0
  cadena = "p \t\t q \t\t p<->q" + "\n"
  while cont != 4:
    if p == q:
      res = True
    else:
      res = False
    cadena += str(p) + "\t\t" + str(q) + "\t\t" + str(res) + "\n"
    c += 1
    if c == 2:
      p = not(p)
    q = not(q)
    cont += 1
  return cadena

# Path: conversiones.py
def bin_a_dec(binario):
  suma =0
  posicion = 0
  #print(f'el binario {binario}')
  while(binario >= 1):
    aux = binario % 10
    binario = binario // 10
    suma=suma + aux * pow(2, posicion);
    posicion += 1
  #print(f'corresponde al numero {suma}')
  return(suma)

def dec_a_bin (decimal):
  d=[]
  while(decimal >= 1):
    d.append(decimal % 2)
    decimal = int(decimal/2)
  s = d[::-1]
  for k in s:
    print(k, end = "")


def dec_a_oct (decimal):
    d=[]
    while(decimal >= 1):
        d.append(decimal % 8)
        decimal = int(decimal/8)
    s = d[::-1]
    for k in s:
        print(k, end = "")

def dec_a_hex (decimal):
    d=[]
    while(decimal >= 1):
        d.append(decimal % 16)
        decimal = int(decimal/16)
    s = d[::-1]
    for k in s:
        print(k, end = "")

def oct_a_dec (octal):
    suma =0
    posicion = 0
    while(octal >= 1):
        aux = octal % 10
        octal = octal // 10
        suma=suma + aux * pow(8, posicion);
        posicion += 1
    return(suma)

def hex_a_dec (hexa):
    suma =0
    posicion = 0
    while(hexa >= 1):
        aux = hexa % 10
        hexa = hexa // 10
        suma=suma + aux * pow(16, posicion);
        posicion += 1
    return(suma)
