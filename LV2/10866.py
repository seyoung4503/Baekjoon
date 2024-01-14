import sys
from collections import deque
input = sys.stdin.readline

dq = deque()
n = int(input())
stack = []
for i in range(n):
    op = []
    op = input().split()

    if op[0] == "push_back":
        dq.append(op[1])

    if op[0] == "push_front":
        dq.appendleft(op[1])

    if op[0] == "front":
        if len(dq) != 0:
            print(dq[0])
        else:
            print(-1)

    if op[0] == "back":
        if len(dq) != 0:
            print(dq[-1])
        else:
            print(-1)

    if op[0] == "size":
        print(len(dq))

    if op[0] == "pop_back":
        if len(dq) != 0:
            print(dq.pop())
        else:
            print(-1)
    
    if op[0] == "pop_front":
        if len(dq) != 0:
            print(dq.popleft())
        else:
            print(-1)

    if op[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)