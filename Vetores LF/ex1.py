'''
1 - Faça um programa que possua um vetor (array) denominado A que armazene 6 números inteiros. 0 programa deve executar os seguintes passos:
Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
Armazene em uma variável inteira (simples) a soma entre todos os valores do vetor.
'''

a = [1, 0, 5, -2, -5, 7]
total = 0
for i in range(0, len(a)):
  total += a[i]

print('total', total)