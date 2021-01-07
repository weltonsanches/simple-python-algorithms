"""
6 - Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa.
"""

arr = [None] * 6
for i in range(len(arr)):
  arr[i] = int(input('Digite um numero: '))

arr.reverse()
print(f'arr reverso {arr}')