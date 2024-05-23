a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

participantes = []
tempos = {}

for _ in range(a):
    nome = input().strip()
    participantes.append(nome)

for _ in range(b):
    sigla, tempo = input().split(" ")
    if sigla not in tempos:
        tempos[sigla] = []
    tempos[sigla].append(tempo)

for _ in range(c):
    sigla, tempo = input().split(" ")
    if sigla in tempos and tempo in tempos[sigla]:
        tempos[sigla].remove(tempo)

menores = []

for participante in participantes:
    sigla = participante[:3].upper()
    if sigla in tempos and tempos[sigla]:
        arr = sorted(tempos[sigla])
        menores.append((arr[0], participante))

menores.sort()

for i, (tempo, participante) in enumerate(menores):
    print(f"{i+1} {tempo} {participante}")
