n = str(input('Qual seu nome completo? ')).strip()
nome = n.split()
print(f'Seu primeiro nome é {nome[0]}')
print('E seu último nome é {}'.format(nome[len(nome)-1]))