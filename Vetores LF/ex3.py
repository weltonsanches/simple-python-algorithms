'''
3 - Escreva um programa que leia 10 números inteiros e o armazene em um vetor.
Imprima o vetor, o maior elemento e a posição que ele se encontra.
'''

arr = [None] * 10
for i in range(len(arr)):
  arr[i] = int(input('Insira um valor '))

# print('O maior elemento é ', max(arr), ' e o índice do maior elemento é ', arr.index(max(arr)));
# Or
max_element = False
for item in arr:
  if max_element < item or not(max_element):
    max_element = item

print(f'O maior elemento é {max_element} e o índice do maior elemento é {arr.index(max_element)}');
