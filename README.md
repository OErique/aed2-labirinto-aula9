# Labirinto - Aula 9 de AED II

Atividade de busca em grafos usando um labirinto 12 x 12 feito para comparar DFS, BFS e busca gulosa. Usei Python e somente bibliotecas que já vêm com ele.

## Como executar

No terminal, dentro da pasta do projeto:

```bash
python main.py
```

O programa imprime o labirinto com o caminho de cada busca (`*`) e, no final, a tabela comparativa. `I` é a entrada, `F` é a saída, `#` é parede e `.` é casa livre.

## Ideia do labirinto

```text
############
#I.........#
#..###.###.#
#..###.###.#
#..#######.#
#..........#
#..###.###.#
#..###.###.#
#..#######.#
#..#########
#.........F#
############
```

Há um trajeto curto descendo pelo lado esquerdo e seguindo pela última linha. Também dá para ir pela parte de cima e atravessar a passagem da linha 5, mas esse trajeto é maior. Os corredores que acabam em parede criam becos sem saída. As coordenadas citadas abaixo começam em zero, como as listas do Python.

Cada casa que não é parede vira um vértice do grafo. As casas vizinhas são examinadas na ordem **cima, direita, baixo, esquerda**, como no slide. A função `montar_grafo` cria as ligações e `desenhar` marca o caminho encontrado. As três buscas guardam de qual casa chegaram a cada vizinho (`pais`); ao achar `F`, a função `reconstruir` segue esses pais de volta até `I` e inverte a lista.

## Comparação

Resultado de `python main.py`:

| Algoritmo | Casas no caminho | Casas visitadas |
| --- | ---: | ---: |
| DFS | 43 | 48 |
| BFS | 19 | 54 |
| Gulosa | 35 | 42 |

O tamanho do caminho inclui a entrada e a saída. Assim, o caminho da BFS tem **18 movimentos** entre casas. Uma casa é contada como visitada quando a busca realmente a processa: na DFS, ao entrar na função recursiva; na BFS e na Gulosa, ao retirá-la da fila. Casas apenas colocadas na fila ainda não entram nessa contagem.

## Para explicar na correção oral

- **BFS:** usa uma fila e percorre as casas por distância a partir da entrada. Como todo movimento custa uma casa, a primeira vez que ela chega à saída corresponde ao menor caminho. Ela visitou mais casas porque explorou outras possibilidades antes de alcançar `F`.
- **DFS:** usa a pilha da recursão e aprofunda a primeira opção disponível. A ordem dos vizinhos faz ela seguir para a direita na parte de cima e percorrer vários corredores antes de chegar à saída. Ela para no primeiro caminho encontrado, que neste caso tem 43 casas, sem comparar com a rota curta da esquerda.
- **Gulosa:** escolhe a casa da fronteira com menor distância de Manhattan até `F`, sem considerar as paredes nessa estimativa. Ela desce pelo corredor da direita até **(8, 10)**, mas **(9, 10)** é parede. A saída parece perto, porém não há passagem por ali. Depois ela encontra a travessia da linha 5 e termina com um caminho de 35 casas. O número menor de visitas não significa caminho menor.
- **Reconstrução:** `pais[vizinho] = casa` registra de onde veio cada casa descoberta. A partir de `F`, seguimos `pais` até `I` e invertimos a sequência para imprimir na ordem de caminhada.
