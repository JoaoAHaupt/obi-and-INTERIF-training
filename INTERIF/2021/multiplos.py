entrada = input()
arrPAR = 0
arrIMPAR = 0

for num in entrada:
    num = int(num)
    if num % 2 == 0:
        arrPAR += num
    else:
        arrIMPAR += num

if arrPAR % 3 == 0:
    print("S")
else:
    print("N")
if arrIMPAR % 3 == 0:
    print("S")
else:
    print("N")