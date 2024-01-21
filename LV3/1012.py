import sys
from collections import deque
input = sys.stdin.readline
cabbages = []


def bfs():

    q = deque()
    q.append(cabbages.pop())
    # print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    # print(q)

    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while len(q) > 0:
        # print(q)
        pos_now = q.popleft()
        # print("pos_now", pos_now)

        pos_next = [0, 0]
        for i in move:
            # print(i)
            pos_next[0] = i[0] + pos_now[0]
            pos_next[1] = i[1] + pos_now[1]
            # print("   pos_next ", pos_next)
            # print(cabbages)
            # print("------------------------------------")
            
            if pos_next in cabbages:
                # print("pos_next ", pos_next)
                q.append(pos_next.copy())
                
                # print(pos_next, cabbages)
                cabbages.remove(pos_next)
                # print("if in ", q)
                # print(pos_next, cabbages)

                # print("pos_next ", pos_next)
            # print("if out ", q, i)






T = int(input())


for i in range(T):
    m, n, k = map(int, input().split())

    
    for i in range(k):
        pos_x, pos_y = map(int, input().split())
        cabbages.append([pos_x, pos_y])

    ans = 0
    while len(cabbages) > 0:
        bfs()
        # print(cabbages)
        ans += 1
    print(ans)



# q = deque()
# q.append([1, 1])
# pos_now = q.popleft()

# print("pos_now", pos_now)

# pos_now[0] = 0

# print(q)