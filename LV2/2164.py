from collections import deque
n = int(input())

l = [i for i in range(1, n+1)]
q = deque(l)
# print(q)

while len(q) > 1:
    q.popleft()
    poped = q.popleft()
    q.append(poped)

print(q[0])
