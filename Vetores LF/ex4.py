'''
4 - Escreva um programa que leia 10 numeros inteiros no intervalo [0,50] e os armazene em um 
vetor estaticamente alocado com 100 posições. Preencha um segundo vetor, também alocado estaticamente, apenas
com os números ímpares do primeiro vetor. Imprima os dois vetores, 10 elementos por linha.
'''

def get_value_between_zero_and_fifty ():
  value = int(input('Insira um valor no intervalo de 0 a 50: '))
  if not(value >= 0 and value <= 50):
    control = True
    while(control):
      value = int(input('O valor inserido estava fora do intervalo, por favor insira um valor entre 0 a 50: '))
      if value >= 0 and value <= 50:
        control = False
  return value

amount_of_integers = int(input('Quantos números você quer digitar? O máximo é 100: '))

if amount_of_integers > 100:
  amount_of_integers = 100

arr = [None] * 100
arr2 = [None] * 100
for i in range(0, amount_of_integers):
  arr[i] = get_value_between_zero_and_fifty()
  if not(arr[i] % 2 == 0):
    arr2[i] = arr[i]

print('Todos os números digitados, 10 por linha')
for i in range(0, len(arr), 10):
  arr_to_show = arr[i:(i + 10)]
  print(', '.join(map(lambda x: str(x), arr_to_show)))

print('Apenas números pares, 10 por linha')
just_odds = list(filter(lambda x: bool(x), arr2))
for i in range(0, len(just_odds), 10):
  odds_to_show = just_odds[i:(i + 10)]
  print(', '.join(map(lambda x: str(x), odds_to_show)))