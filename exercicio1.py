
preco = float(input('Digite o preço do produto: '))
percentual = float(input('Digite o percentual de desconto (0-100%): '))

desconto = preco * (percentual / 100)
final = preco - desconto

print(f'O preco do produto é R$ {preco:.2f}. Desconto de {percentual}%.')
print(f'Valor calculado de desconto: R$ {desconto:.2f}. Valor final do produto: R$ {final:.2f}')
