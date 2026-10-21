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

## Observações sobre os resultados

A BFS usa uma fila e percorre as casas por distância a partir da entrada. Como todo movimento tem o mesmo custo, ela encontra primeiro o caminho mais curto: 19 casas. A DFS usa a pilha da recursão e segue a primeira opção disponível até não conseguir continuar. Pela ordem dos vizinhos, ela vai para a direita na parte de cima e encontra uma rota de 43 casas antes de tentar a rota curta da esquerda.

A busca gulosa usa a distância de Manhattan até `F` para escolher qual casa examinar em seguida. Essa conta ignora as paredes. No corredor da direita, ela chega a **(8, 10)**, mas a casa **(9, 10)** é parede. Depois precisa encontrar a passagem pela linha 5, por isso seu caminho ficou com 35 casas. Ela visitou menos casas que a BFS, mas encontrou um caminho maior.

Para formar qualquer um dos caminhos, cada busca registra `pais[vizinho] = casa` quando descobre uma casa. A partir de `F`, o programa segue essas referências até `I` e inverte a sequência.
