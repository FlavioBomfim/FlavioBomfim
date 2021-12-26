import random
a1= input('Quem é o primeiro aluno? ')
a2= input('Quem é o segundo aluno? ')
a3= input('Quem é o terceiro aluno? ')
a4= input('Quem é o quarto aluno? ')
lista= [a1, a2, a3, a4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')