"""
12 - Faça um programa que receba 6 números inteiros e mostre:
 - Os números pares digitados;
 - A soma dos números pares digitados;
 - Os números impares digitados;
 - A quantidade de números ímpares digitados.
"""
from functools import reduce

def arr_sum (a, b):
  return a + b

arr = [None] * 6
for i in range(len(arr)):
  arr[i] = int(input(f'Insira um número: '))

just_even = [i for i in arr if i % 2 == 0]
just_odd = [i for i in arr if i % 2 != 0]
total_even = reduce(arr_sum, just_even)
amount_of_odd = len(just_odd)

print(f'Números pares digitados: {just_even}')
print(f'A soma dos números pares digitados: {total_even}')
print(f'Números impares digitados: {just_odd}')
print(f'A quantidade de números impares digitados: {amount_of_odd}')