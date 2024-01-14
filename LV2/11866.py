import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
ans = []
dq = deque(i for i in range(1, n+1))

while len(dq) > 1:
    for i in range(k-1):
        dq.rotate(-1)

    ans.append(dq.popleft())

ans.append(dq.popleft())
result = ", ".join(map(str, ans))
print("<" + result + ">")
