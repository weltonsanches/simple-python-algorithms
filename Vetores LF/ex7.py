"""
7 - Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos na ordem inversa.
"""
def check_odds (number):
  return True if number % 2 == 0 else False

def get_value_odd ():
  value = int(input('Insira um valor par: '))
  if not(check_odds(value)):
    control = True
    while(control):
      value = int(input('O valor é impar seu burro, insira um valor par: '))
      if check_odds(value):
        control = False
  return value

arr = [None] * 6
for i in range(0, len(arr)):
  arr[i] = get_value_odd()

arr.reverse()
print('arr inverso', arr)