vezes = int(input())
quantidades = []
precos = []
lucro = 0

for _ in range(vezes):
    quantidade, preco = map(int, input().split())
    quantidades.append(quantidade)
    precos.append(preco)

for i in range(len(quantidades)):
    lucro += (quantidades[i] * precos[i])

vendaPreco = float(input())
lair = abs(lucro - vendaPreco * sum(quantidades))

print("{:.2f}".format(lair))
if lucro > 20000:
    print("{:.2f}".format(lair*15/100))
else:
    print("0.00")