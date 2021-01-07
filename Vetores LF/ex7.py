"""
7 - Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos na ordem inversa.
"""
def check_even (number):
  return True if number % 2 == 0 else False

def get_value_even ():
  value = int(input('Insira um valor par: '))
  if not(check_even(value)):
    control = True
    while(control):
      value = int(input('O valor é impar seu burro, insira um valor par: '))
      if check_even(value):
        control = False
  return value

arr = [None] * 6
for i in range(len(arr)):
  arr[i] = get_value_even()

arr.reverse()
print(f'arr inverso {arr}')