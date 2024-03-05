import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

map_ = []

start_pos = [-1, -1]
isDiscover = False
for i in range(n):
    sub_map = list(map(int, input().split()))
    
    if isDiscover == False:
        for element_pos in range(m):
            if sub_map[element_pos] == 2:
                start_pos[0] = i
                start_pos[1] = element_pos

                isDiscover = True
                break

    map_.append(sub_map)


# print(start_pos)

visit = [[0 for j in range(m)] for i in range(n)]
distance_value = [[-1 for j in range(m)] for i in range(n)]



# visit[start_pos[0]][start_pos[1]] = 1

distance_value[start_pos[0]][start_pos[1]] = 0
q = deque()


def distance():
    q.append(start_pos)
    visit[start_pos[0]][start_pos[1]] = 1


    while len(q) > 0:
        pos_now = q.popleft()
        # visit[pos_now[0]][pos_now[1]] = 1

        for i in range(4):
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]

            pos_now_x = pos_now[0]
            pos_now_y = pos_now[1]

            pos_next_x = pos_now_x + dx[i]
            pos_next_y = pos_now_y + dy[i]

            if (0 <= pos_next_x < n) and (0 <= pos_next_y < m) and visit[pos_next_x][pos_next_y] == 0:
                
                distance_value[pos_next_x][pos_next_y] = 0
                
                if map_[pos_next_x][pos_next_y] > 0:
                    
                    distance_value[pos_next_x][pos_next_y] = distance_value[pos_now_x][pos_now_y] + 1
                    visit[pos_next_x][pos_next_y] = 1
                    q.append([pos_next_x, pos_next_y])
                
                
distance()


for i in range(n):
    for j in range(m):
        if visit[i][j] == 0 and map_[i][j] == 0:
            distance_value[i][j] = 0


for row in distance_value:

    for i in row:
        print(i, end=" ")
    print()

# for i in range(n):

#     print(*visit[i])