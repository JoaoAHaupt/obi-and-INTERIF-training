[linhas, colunas] = list(map(int, input().split(' ')))
matriz = []
dict = {}

for _ in range(linhas):
    entrada_linha = input().split(" ")
    matriz.append(entrada_linha)

palavras = input().split(" ")


for palavra in palavras:
    dict[palavra] = 0

for palavra in palavras:
    for linha in range(linhas):
        if palavra in "".join(matriz[linha]):
            dict[palavra] = dict[palavra] + 1
    for coluna in range(colunas):
        coluna_atual = "".join(matriz[linha][coluna] for linha in range(linhas))
        if palavra in coluna_atual:
            dict[palavra] += 1

for lepo in dict:
    print(f"{lepo}: {dict[lepo]}")