"""
9 - Fazer um programa para ler 5 valores, e, em seguida, mostrar a posição onde se encontram o maior e o menor valor.
"""

arr = [None] * 5
for i in range(len(arr)):
  arr[i] = int(input('Insira um valor '))

bigger = None
smaller = None
for i in range(len(arr)):
  if bigger == None or bigger < arr[i]:
    bigger = i
  
  if smaller == None or smaller > arr[i]:
    smaller = i

print(f'O maior valor fica no índice {bigger}. O menor valor fica no índice {smaller}.')