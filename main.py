"""Atividade da aula 9: caminhos em um labirinto."""

from collections import deque
import heapq


# I = entrada, F = saída, # = parede, . = casa livre.
labirinto = [
    "############",
    "#I.........#",
    "#..###.###.#",
    "#..###.###.#",
    "#..#######.#",
    "#..........#",
    "#..###.###.#",
    "#..###.###.#",
    "#..#######.#",
    "#..#########",
    "#.........F#",
    "############",
]

DIRECOES = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # cima, direita, baixo, esquerda


def achar(lab, simbolo):
    for i, linha in enumerate(lab):
        if simbolo in linha:
            return (i, linha.index(simbolo))


def livre(lab, i, j):
    dentro = 0 <= i < len(lab) and 0 <= j < len(lab[0])
    return dentro and lab[i][j] != '#'


def montar_grafo(lab):
    grafo = {}
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if not livre(lab, i, j):
                continue
            grafo[(i, j)] = []
            for di, dj in DIRECOES:
                if livre(lab, i + di, j + dj):
                    grafo[(i, j)].append((i + di, j + dj))
    return grafo


def desenhar(lab, caminho):
    grade = [list(linha) for linha in lab]
    for i, j in caminho:
        if grade[i][j] == '.':
            grade[i][j] = '*'
    for linha in grade:
        print(''.join(linha))


def reconstruir(pais, saida):
    """Volta do fim até a entrada usando o pai de cada casa."""
    caminho = []
    atual = saida
    while atual is not None:
        caminho.append(atual)
        atual = pais[atual]
    caminho.reverse()
    return caminho


def dfs(grafo, inicio, saida):
    visitados = set()
    pais = {inicio: None}

    def visitar(casa):
        visitados.add(casa)
        if casa == saida:
            return True
        for vizinho in grafo[casa]:
            if vizinho not in visitados:
                pais[vizinho] = casa
                if visitar(vizinho):
                    return True
        return False

    encontrou = visitar(inicio)
    return (reconstruir(pais, saida) if encontrou else [], len(visitados))


def bfs(grafo, inicio, saida):
    fila = deque([inicio])
    pais = {inicio: None}  # também marca as casas já descobertas
    visitadas = 0
    while fila:
        casa = fila.popleft()
        visitadas += 1
        if casa == saida:
            return reconstruir(pais, saida), visitadas
        for vizinho in grafo[casa]:
            if vizinho not in pais:
                pais[vizinho] = casa
                fila.append(vizinho)
    return [], visitadas


def distancia_manhattan(casa, saida):
    return abs(casa[0] - saida[0]) + abs(casa[1] - saida[1])


def gulosa(grafo, inicio, saida):
    # O contador desempata prioridades iguais pela ordem em que entraram.
    fronteira = [(distancia_manhattan(inicio, saida), 0, inicio)]
    pais = {inicio: None}
    visitadas = 0
    contador = 0
    while fronteira:
        _, _, casa = heapq.heappop(fronteira)
        visitadas += 1
        if casa == saida:
            return reconstruir(pais, saida), visitadas
        for vizinho in grafo[casa]:
            if vizinho not in pais:
                pais[vizinho] = casa
                contador += 1
                heapq.heappush(
                    fronteira,
                    (distancia_manhattan(vizinho, saida), contador, vizinho),
                )
    return [], visitadas


def main():
    inicio = achar(labirinto, 'I')
    saida = achar(labirinto, 'F')
    grafo = montar_grafo(labirinto)
    resultados = []

    for nome, algoritmo in [('DFS', dfs), ('BFS', bfs), ('Gulosa', gulosa)]:
        caminho, visitadas = algoritmo(grafo, inicio, saida)
        print(f'\n{nome}:')
        desenhar(labirinto, caminho)
        resultados.append((nome, len(caminho), visitadas))

    print('\nAlgoritmo | Casas no caminho | Casas visitadas')
    print('----------|------------------|----------------')
    for nome, tamanho, visitadas in resultados:
        print(f'{nome:<9} | {tamanho:>16} | {visitadas:>15}')
    print('\nObs.: o tamanho conta I e F; as visitas contam casas retiradas da busca.')


if __name__ == '__main__':
    main()
