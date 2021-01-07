"""
9 - Fazer um programa para ler 5 valores, e, em seguida, mostrar a posição onde se encontram o maior e o menor valor.
"""

arr = [None] * 5
for i in range(0, len(arr)):
  arr[i] = int(input('Insira um valor '))

bigger = None
smaller = None
for i in range(0, len(arr)):
  if bigger == None or bigger < arr[i]:
    bigger = i
  
  if smaller == None or smaller > arr[i]:
    smaller = i

print('O maior valor fica no índice', bigger, 'o menor valor fica no índice', smaller)