import heapq, sys

n = int(input())
heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(heap, x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)