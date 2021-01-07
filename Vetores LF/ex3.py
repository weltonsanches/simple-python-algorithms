'''
3 - Escreva um programa que leia 10 números inteiros e o armazene em um vetor.
Imprima o vetor, o maior elemento e a posição que ele se encontra.
'''

arr = [None] * 10
for i in range(0, len(arr)):
  arr[i] = int(input('Insira um valor '))

# print('O maior elemento é ', max(arr), ' e o índice do maior elemento é ', arr.index(max(arr)));
# Or
max_element = False
for i in range(0, len(arr)):
  if max_element < arr[i] or not(max_element):
    max_element = arr[i]

print('O maior elemento é ', max_element, ' e o índice do maior elemento é ', arr.index(max_element));
