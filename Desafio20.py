import random
a1 = str(input('Primeiro aluno '))
a2 = str(input('Segundo aluno '))
a3 = str(input('terceiro aluno '))
a4 = str(input('quarto aluno '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem será: {}'.format(lista))