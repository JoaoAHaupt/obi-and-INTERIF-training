a, b, c = input().split(" ")
i = 0
dict = {}
participantes = []

while i != int(a):
    nome = input()
    participantes.append(nome)
    i += 1
i = 0

while i != int(b):
    sigla, tempo = input().split(" ")
    if sigla not in dict:
        dict[sigla] = []
    dict[sigla].append(tempo)
    i += 1

i = 0
while i != int(c):
    sigla, tempo = input().split(" ")
    arr = dict[sigla]
    arr.remove(tempo)
    i += 1

menores = {}
for participante in participantes:
    arr = sorted(dict[participante[:3].upper()])
    menores[arr[0]] = participante

for i, participante in enumerate(sorted(menores.keys())):
    print(f"{i+1} {participante} {menores[participante]}")


