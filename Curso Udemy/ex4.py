'''
4 - Escreva um programa que ordene uma lista numérica com três elementos.
'''
arr = [None] * 3
for i in range(0, len(arr)):
  arr[i] = input('Insira um valor ')

arr.sort()
print(arr)