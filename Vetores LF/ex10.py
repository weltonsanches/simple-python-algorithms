"""
10 - Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que possuirem valores negativos.
"""

arr = [None] * 10
for i in range(len(arr)):
  value = int(input('Insira um valor '))
  arr[i] = 0 if value < 0 else value

print(arr)