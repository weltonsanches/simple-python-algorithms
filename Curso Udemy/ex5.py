'''
5 - Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.
'''

n1 = int(input('Insira o primeiro número da operação: '))
operation = input('Insira o sinal da operação (disponíveis +, -, x e /): ')
n2 = int(input('Insira o segundo número da operação: '))

if operation == '+':
  print(n1 + n2)
elif operation == '-':
  print(n1 - n2)
elif operation == 'x':
  print(n1 * n2)
elif operation == '/':
  print(n1 / n2)
else:
  print('Operação não reconhecida')