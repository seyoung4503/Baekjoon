import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

visited = [0 for _ in range(100001)]

visited[n] = 1

def bfs():
    q = deque()
    q.append([n, 0])
    count = 100001

    while len(q) > 0 and count >= 0:
        present_node, present_time = q.popleft()
        if present_node == k:
            print(present_time)
            return
        count -= 1

        next_node = [present_node-1, present_node+1, present_node*2]

        for next_idx in next_node:
            if (next_idx <= 100000 and next_idx >= 0) and visited[next_idx] == 0:
                q.append([next_idx, present_time+1])
                visited[next_idx] = 1

bfs()

# q = deque()
# q.append([1, 'a'])
# q.append([2, 'b'])
# print(q)


# dp = [100000 for _ in range(100001)]
# visit = [0 for _ in range(100001)]

# dp[0] = 0
# dp[n] = 1
# visit[5] = 1

# ans = []
# def dpdp(idx, prev):
#     if idx == 0 or idx == 100001:
#         return
#     if idx == k:
#         ans.append(dp[idx]-1)
#         return
#     next_idx = [idx-1, idx+1, idx*2]
#     # sum(visit) < 100001
#     x = 0
#     while x < 100:
#         for i in next_idx:
#             dp[i] = min(dp[i], dp[prev] + 1)
#             visit[i] = 1
#         prev = idx
#         x += 1
#     # dpdp(idx-1, idx)
#     # dpdp(idx+1, idx)
#     # dpdp(idx*2, idx)


# dpdp(n, n)
# print(dp[n])
