import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    inputs = int(input())
    if inputs == 0:
        stack.pop()
    else:
        stack.append(inputs)

print(sum(stack))