import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

data = {}
for i in range(m):
    key, value = map(int, input().split())

    if key in data:
        values = data[key]
        values.add(value)
        data[key] = values
    else:
        data[key] = set([value])

    
    if value in data:
        values = data[value]
        values.add(key)
        data[value] = values
    else:
        data[value] = set([key])

# print(data)


kevin = []
for i in range(1, n+1):
    
    counts = [0 for i in range(n+1)]
    # visits = counts[:]
    # dfs
    q = deque()
    q.append(i)

    # start dfs

    count = 0
    while len(q) > 0:
        now = q.popleft()
        
        next_nodes = data[now]


        for next_node in next_nodes:

            if counts[next_node] == 0 :

                q.append(next_node)
                counts[next_node] = counts[now] + 1

    kevin.append(sum(counts))


print(kevin.index(min(kevin))+ 1)



# 1 3, 4              2 + 1 + 1 + 2 = 6
# 2 3                 2 + 1 + 3 + 4
# 3 1, 2, 4           1 + 1 + 2 + 3
# 4 1, 3, 5           
# 5 4