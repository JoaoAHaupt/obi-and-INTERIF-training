pontos = {1: 5, 2: 10, 3: 15, 4: 20, 5: 50}
respostas =[]

while True:
    arr = {1: [], 2: [], 3: []}

    comeco = int(input())
    if comeco == -1:
        break
    varetas = list(map(int, input().split(' ')))
    for vareta in varetas:
        if vareta == -1:
            break
        if vareta == 0:
            if comeco == 3:
                comeco = 1
            else:
                comeco += 1
        else:
            arr[comeco].append((pontos[vareta]))

    for participante in arr:
        arr[participante] = sum(arr[participante])

    arr = dict(sorted(arr.items(), key=lambda item: item[1], reverse=True))

    final = "Ganhador"
    colocacao = []

    for i in arr:
        if arr[i] == max(arr.values()):
            colocacao.append(f"Jogador {i}")
            final = "Empate"

    respostas.append(f"""{final} com {max(arr.values())} pontos {', '.join(colocacao)}""")

for resposta in respostas:
    print(resposta)
