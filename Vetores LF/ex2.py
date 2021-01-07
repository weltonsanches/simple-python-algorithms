'''
2 - Faça um programa que possua um vetor (array) denominado A que armazene 6 números inteiros. 0 programa deve executar os seguintes passos:
Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
Armazene em uma variável inteira (simples) a soma entre os valores das posições A[0], A[1] e A[5] do vetor, e mostre na tela esta soma.
Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
Mostre na tela cada valor do vetor A, um em cada linha.
'''

a = [1, 0, 5, -2, -5, 7]
sum_of_some_positions = a[0] + a[1] + a[5]
print(f'soma entre os valores das posições A[0], A[1] e A[5] do vetor {sum_of_some_positions}')
a[4] = 100
for i in a:
  print('a', i)