import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    op = []
    op = input().split()

    if op[0] == "push":
        stack.append(op[1])

    if op[0] == "front":
        if len(stack) != 0:
            print(stack[0])
        else:
            print(-1)

    if op[0] == "back":
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)

    if op[0] == "size":
        print(len(stack))

    if op[0] == "pop":
        if len(stack) != 0:
            print(stack.pop(0))
        else:
            print(-1)

    if op[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)