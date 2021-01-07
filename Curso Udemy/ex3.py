'''
3 - Escreva um programa que resolva uma equação de segundo grau (equação de báscara).
'''
from math import sqrt

a = int(input('Digita um número para A: '))
b = int(input('Digita um número para A: '))
c = int(input('Digita um número para A: '))

delta = b**2 -4 * a * c
raiz_delta = sqrt(delta) if delta >= 0 else -1

if raiz_delta < 0:
  print('Delta negativo')
else:
  x1 = (-b + delta) / (2 * a)
  x2 = (-b - delta) / (2 * a)

  print('As raízes são', str(round(x1, 2)), 'e', str(round(x2, 2)))
