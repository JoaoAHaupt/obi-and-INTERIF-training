cardias = {
    "-1": [],
    "-2": [],
    "-3": [],
    "-4": []
}
ultimo = ""
aviao = []
lados = ["-1", "-3", "-2", "-4"]

while True:
    entrada = input()
    if entrada == "0":
        break
    if entrada in lados:
        ultimo = entrada
    else:
        cardias[ultimo].append(entrada)

while True:
    todos_vazios = True

    for lado in lados:
        if cardias[lado]:
            todos_vazios = False
            aviao.append(cardias[lado].pop(0))

    if todos_vazios:
        break

print(" ".join(aviao))
