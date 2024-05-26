grafo = {}
pais = {}
custos = {}
processados = []


[cidades, ligacoes] = list(map(int, input().split(' ')))
[inicio, fim] = list(map(int, input().split(' ')))

custos[fim] = float("inf")
pais[fim] = None

for _ in range(ligacoes):
    [cidade1, tempo, cidade2] = list(map(int, input().split(' ')))
    if cidade1 not in grafo:
        grafo[cidade1] = {}
    grafo[cidade1][cidade2] = tempo
    custos[cidade1] = tempo

print(grafo)
print(custos)


def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

nodo = ache_no_custo_mais_baixo(custos)
while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos)

print(novo_custo)
