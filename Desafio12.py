preco= float(input('Digite o valor do produto '))
desconto= float(input('Digite o desconto '))
result= preco*desconto/100
vf= preco-result
print(f'O preço era {preco}R$ e o desconto é de {desconto}% então o preço final é: {vf}R$ ')

