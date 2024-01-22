import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
edge = []
for i in range(M):
    x = list(map(int, input().split()))
    edge.append(x)

vertex = [0 for i in range(N+1)]

edge = list(set([tuple(set(edge)) for edge in edge]))
edge.sort()
# print(edge)

ans_bfs = []
ans_dfs = []
def bfs():
    q = deque()
    q.append(V)
    vertex[V] = 1

    while len(q) > 0:
        v_now = q.popleft()
        ans_bfs.append(v_now)

        v_next = []
        for i in range(len(edge)):
            x, y = edge[i][0], edge[i][1]

            
            if x == v_now and vertex[y] == 0:
                v_next.append(y)
                vertex[y] = 1
            if y == v_now and vertex[x] == 0:
                v_next.append(x)
                vertex[x] = 1
            
        v_next.sort()
        for i in v_next:
            q.append(i)

def dfs():
    edge.sort(reverse=True)
    # print(edge)
    stack = []
    # vertex[V] = 1

    stack.append(V)
    
    while len(stack) > 0:
        v_now = stack[-1]
        if vertex[v_now] == 0:
            ans_dfs.append(v_now)   
        
        v_next = []

        flag = False
        vertex[v_now] = 1
        for x, y in edge:
            # x, y = edge[i][0], edge[i][1]

            if x == v_now and vertex[y] == 0:
                v_next.append(y)
                flag = True
            elif y == v_now and vertex[x] == 0:
                v_next.append(x)
                flag = True
        
        if len(v_next) > 0:
            stack.append(min(v_next))
        
        if flag == False:
            stack.pop()
    
        # print(stack)


dfs()
vertex = [0 for i in range(N+1)]
bfs()

for i in ans_dfs:
    print(i, end=" ")
print()
for i in ans_bfs:
    print(i, end=" ")
print()
