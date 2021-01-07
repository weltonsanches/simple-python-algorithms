"""
8 - Fazer um programa para ler 5 valores, e, em seguida, mostrar todos os valores lidos juntamente com o maior, 
o menor e a média dos valores.
"""

arr = [None] * 5
for i in range(0, len(arr)):
  arr[i] = int(input('Insira um valor '))

bigger = None
smaller = None
total = 0
for i in range(0, len(arr)):
  if bigger == None or bigger < arr[i]:
    bigger = arr[i]
  
  if smaller == None or smaller > arr[i]:
    smaller = arr[i]

  total += arr[i]

average = total / len(arr)

print('O maior valor é', bigger, 'o menor valor é', smaller, 'a média dos valores é', average)