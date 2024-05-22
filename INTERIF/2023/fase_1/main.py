vogal = 'aeiou'

animal = input().lower()
i = 0
for letra in animal:
    if letra in vogal:
        i += 1

print(f'frasco {i%3}')