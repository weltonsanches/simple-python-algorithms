'''
5 - Leia um vetor de 10 posições, contar e escrever quantos valores pares ele possui
'''

def check_even (number):
  return True if number % 2 == 0 else False

arr = [None] * 10
for i in range(len(arr)):
  arr[i] = int(input('Digite um numero: '))

just_even = list(filter(check_even, arr))

print(f'Tem {len(just_even)} pares. Os pares são {just_even}')