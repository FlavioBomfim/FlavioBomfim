import math
an = float(input('Digite o ângulo que vc deseja: '))
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
print('O seno de {} é {:.2f}'.format(an, seno))
print('O cosseno é de {:.2f}'.format(cos))
tang= math.tan(math.radians(an))
print('E a tangente é {:.2f}'.format(tang))