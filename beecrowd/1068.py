entrada = input()

saida = "correct"
direita = []
esquerda = []

for i in entrada:
    if i == "(":
        esquerda.append(i)
    elif i == ")":
        try:
            esquerda.pop()
        except:
            saida = "incorrect"
            break

if len(direita) != len(esquerda):
    saida = "incorrect"
print(saida)
