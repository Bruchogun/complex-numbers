import math
def inputComplex():
    userInput = input('Ingrese un complejo: ')
    userInput = userInput.split('+')
    userInput[1] = userInput[1].replace('i','')
    complex = [float(userInput[0]),float(userInput[1])]
    return complex

def division(complexA,complexB):
  resultReal = round((complexA[0]*complexB[0] + complexA[1]*complexB[1]) / (complexB[0]**2 + complexB[1]**2),4)
  resultImg = round((complexA[1]*complexB[0] - complexA[0]*complexB[1]) / (complexB[0]**2 + complexB[1]**2),4)
  return [resultReal,resultImg]

def addition(complexA,complexB):
  resultReal = round(complexA[0] + complexB[0],4)
  resultImg = round(complexA[1] + complexB[1],4)
  return [resultReal,resultImg]

def multiplication(complexA,complexB):
  resultReal = round(( complexA[0]*complexB[0] - complexA[1]*complexB[1] ),4)
  resultImg = round(( complexA[0]*complexB[1] + complexA[1]*complexB[0] ),4)
  return [resultReal,resultImg]

def module(complex):
  complex[0] = float(complex[0])
  complex[1] = float(complex[1])
  result = round((complex[0]**2 + complex[1]**2)**(1/2),4)
  return result

def conjugate(complex):
  result = round(-complex[1],4)
  return result

def cartesian2polar(complex):
  r = module(complex)
  angle = round(math.atan2(complex[1],complex[0]),4)
  return [r,angle]

def polar2cartesian(complex):
  a = round(complex[0]*math.cos(complex[1]),4)
  b = round(complex[0]*math.sin(complex[1]),4)
  return [a,b]

def phase(complex):
  phase = round(math.atan2(complex[1],complex[0]),4)
  return phase

# complexA - complexB
def subtraction(complexA,complexB):
  resultReal = round(complexA[0] - complexB[0],4)
  resultImg = round(complexA[1] - complexB[1],4)
  return [resultReal,resultImg]

def prettyPrinting(label,data):
  print(label,data[0],'+',data[1],'i')