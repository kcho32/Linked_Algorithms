import sys
import heapq
input = sys.stdin.readline

nodes, roads = map(int, input().split())
graph = [[] for _ in range(nodes + 1)]
INF = int(1e9)
for i in range(roads):
    f, t, dist = map(int, input().split())
    graph[f].append((dist, t))
    graph[t].append((dist, f))
must_visit1, must_visit2 = map(int, input().split())

def dijkstra(start, final):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF for __ in range(nodes + 1)]
    distance[start] = 0
    while q:
        dist, current = heapq.heappop(q)
        if distance[current] < dist:
            continue
        for destination in graph[current]:
            total_dist = destination[0] + dist
            if total_dist < distance[destination[1]]:
                distance[destination[1]] = total_dist
                heapq.heappush(q, (total_dist, destination[1]))
    return distance[final]
first = dijkstra(1, must_visit1) + dijkstra(must_visit1, must_visit2) + dijkstra(must_visit2, nodes)
second = dijkstra(1, must_visit2) + dijkstra(must_visit2, must_visit1) + dijkstra(must_visit1, nodes)

if not nodes == must_visit1 and not nodes == must_visit2:
    answer = min(first, second)
    
elif nodes == must_visit1 and nodes != must_visit2:
    answer = second

elif nodes == must_visit2 and nodes != must_visit1:
    answer = first

if answer > INF or roads == 0:
    answer = -1
if nodes == 1:
    answer = 0
print(answer)
