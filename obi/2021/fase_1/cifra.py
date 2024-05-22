

palavra = input()
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
consoantes = 'bcdfghjklmnpqrstvxz'

vogais = 'aeiou'
arr = []

for letra in palavra:
    arr.append(letra)
    if letra not in vogais:
        index = consoantes.index(letra)

        lepo = {}
        for vogal in vogais:
            lepo[vogal] = abs(alfabeto.index(letra) - alfabeto.index(vogal))

        chave_min_valor = min(lepo, key=lepo.get)

        arr.append(chave_min_valor)

        if index < len(consoantes) - 1:
            proxima = consoantes[index + 1]
            arr.append(proxima)


print(''.join(arr))
