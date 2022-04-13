import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
nums = Counter({})

for i in list(map(int, sys.stdin.readline().rstrip().split(" "))):
    nums[i] += 1

m = int(sys.stdin.readline().rstrip())
for j in list(map(int, sys.stdin.readline().rstrip().split(" "))):
    print(nums[j], end=" ")