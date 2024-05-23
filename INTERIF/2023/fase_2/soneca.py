n, h, c, a = map(int, input().split())
sequencia2 = list(map(int, input().split()))

if sequencia2[(a // h) % n] >= c:
    print("O vilarejo de Faz-de-contIF foi alertado")
else:
    print("O vilarejo de Faz-de-contIF foi devorado")
