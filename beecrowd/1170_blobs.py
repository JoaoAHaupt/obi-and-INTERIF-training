vezes = int(input())
i = 0
arr = []
while i < vezes:
    x = 0
    comida = float(input())

    while comida > 1:
        x += 1
        comida /= 2

    arr.append(str(x) + " dias")
    i += 1

for i in arr:
    print(i)