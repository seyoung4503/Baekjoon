import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
ans = []

for i in range(n):
    
    N, M = map(int, input().split())
    priority = deque(map(int, input().split()))
    papers = deque([i for i in range(1,N+1)])
    
    next_paper = max(priority)
    
    times = 0
    while len(papers) != 0:
        next_paper = max(priority)
        if next_paper == priority[0]:
            x = priority.popleft()
            y = papers.popleft()
            times += 1

            if (y-1) == M:
                ans.append(times)
        else:
            priority.rotate(-1)
            papers.rotate(-1)

for i in ans:
    print(i)
