import math
co = float(input('Qual o tamanho do cateto '))
ca = float(input('Qual o valor do outro cateto '))
h = (co**2 + ca**2) ** (1/2)
print('A hipotenusa será {:.1f}'.format(h))