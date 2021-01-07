'''
5 - Leia um vetor de 10 posições, contar e escrever quantos valores pares ele possui
'''

def check_odds (number):
  return True if number % 2 == 0 else False

arr = [None] * 10
for i in range(0, len(arr)):
  arr[i] = int(input('Digite um numero: '))

just_odds = list(filter(check_odds, arr))

print('Tem', len(just_odds), 'pares. Os pares são ', just_odds)