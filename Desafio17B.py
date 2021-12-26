import math
co = float(input('Qual o tamanho do cateto '))
ca = float(input('Qual o valor do outro cateto '))
h = math.hypot(co, ca)
print(f'A hipotenusa será: {h}')