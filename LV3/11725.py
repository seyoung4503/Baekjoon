import sys
sys.setrecursionlimit(10**9)
from collections import deque
input = sys.stdin.readline

n = int(input())

data = {}
for i in range(n-1):
    a, b = map(int, input().split())
    key_ = data.keys()
    if a in key_:
        data[a].append(b)
    else:
        data[a] = [b]

    if b in key_:
        data[b].append(a)

    else:
        data[b] = [a]

# print(data)

parent_num = [0 for i in range(n+1)]
visited = [0 for i in range(n+1)]
visited[1] = 1
def dfs(parent):
    child = data[parent]
    # visited[parent] = 1

    for i in child:
        if visited[i] == 0:
            parent_num[i] = parent
            visited[i] = 1

            dfs(i)
            # visited[i] = 0

dfs(1)

for i in range(2, n+1):
    print(parent_num[i])