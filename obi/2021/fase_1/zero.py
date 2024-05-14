vezes = int(input())
i = 0
arr = []
while i < vezes:
    entrada = int(input())
    if entrada != 0:
        arr.append(entrada)
    else:
        if len(arr) == 0:
            pass
        else:
            arr.pop()
    i += 1
print(sum(arr))