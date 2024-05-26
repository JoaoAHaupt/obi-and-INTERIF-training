entrada = input().lower()
saidas = []
while True:
    if entrada == "*":
        break
    arr = entrada.split(" ")
    count = 0
    palavra = ""
    for i in range(len(arr)):
        palavra += arr[i][0]

    for i in range(len(palavra)):
        if palavra[0] != palavra[i]:
            saidas.append("N")
            break
        elif i == len(palavra) - 1:
            saidas.append("Y")

    entrada = input().lower()

for saida in saidas:
    print(saida)
