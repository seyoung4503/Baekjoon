import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())

tomato_box = []
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# start_pos = []
q = deque()
for i in range(n):
    sub = list(map(int, input().split()))
    tomato_box.append(sub)

    for j in range(m):
        if sub[j] == 1:
            q.append((i, j))

# print(q)

while len(q) > 0:
    now = q.popleft()
    
    next_node = [0, 0]
    for i in range(4):
        next_node[0] = now[0] + direction[i][0]
        next_node[1] = now[1] + direction[i][1]

        if (0 <= next_node[0] < n) and (0 <= next_node[1] < m) and tomato_box[next_node[0]][next_node[1]] == 0:

            tomato_box[next_node[0]][next_node[1]] = tomato_box[now[0]][now[1]] + 1
            
            q.append((next_node[0], next_node[1]))

isRipens = True
max_list = []
for i in range(n):
    max_list.append(max(tomato_box[i]))
    for j in range(m):

        if tomato_box[i][j] == 0:
            isRipens = False
            break
    
    if isRipens == False:
        break

if isRipens:
    print(max(max_list)-1)
else:
    print(-1)



