import heapq, sys

n = int(input())
heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)