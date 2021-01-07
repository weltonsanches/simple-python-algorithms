"""
11 - Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral.
"""

score = [None] * 15
total = 0
for i in range(len(score)):
  score[i] = float(input(f'Insira a nota do aluno {i+1}: '))
  total += score[i]

average = total / 15
print(f'A média das notas de todos os alunos é {average}')