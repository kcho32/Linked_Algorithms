import sys
input = sys.stdin.readline

cities, roads = map(int, input().split())
INF = int(1e9)
graph = [[INF for _ in range(cities + 1)] for __ in range(cities + 1)]
answer = INF

for i in range(1, cities + 1):
    for j in range(1, cities + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(roads):
    f, t, cost = map(int, input().split())
    graph[f][t] = min(cost, graph[f][t])

for k in range(1, cities + 1):
    for a in range(1, cities + 1):
        for b in range(1, cities + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for start in range(1, cities + 1):
    for end in range(1, cities + 1):
        if start == end:
            continue
        answer = min(graph[start][end] + graph[end][start], answer)

if answer >= INF:
    answer = -1

print(answer)