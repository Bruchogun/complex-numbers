import math
def inputComplex(user_input):
  while True:
      if user_input:
        user_input = user_input.replace(' ', '').split(',')
      else:
        user_input = input('Enter a complex number (e.g., 1+2i): ').replace(' ', '').split(',')
      real = float(user_input[0]) 
      imag = float(user_input[1]) 
      return [real, imag]

def division(complexA,complexB):
  try:
    resultReal = round((complexA[0]*complexB[0] + complexA[1]*complexB[1]) / (complexB[0]**2 + complexB[1]**2),4)
    resultImg = round((complexA[1]*complexB[0] - complexA[0]*complexB[1]) / (complexB[0]**2 + complexB[1]**2),4)
    return [resultReal,resultImg]
  except ZeroDivisionError:
    return 'No se puede dividir por 0'

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