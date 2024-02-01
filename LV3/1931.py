import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr = sorted(arr, key = lambda x: (x[1], x[0]))
# print(arr)

visited = []

dp = [0 for _ in range(n)]
dp[0] = 1
count = 1

ans = [arr[0]]
for i in range(1, n):
    x = arr[i][0]
    y = arr[i][1]

    
    if ans[-1][1] <= x:
        ans.append(arr[i])
        count += 1

# print(ans)
print(count)
    

# 1  4   1
# 3  5   1
# 0  6   1
# 5  7   2
# 3  8   1
# 5  9   2
# 6  10  2
# 8  11  3
# 8  12  3
# 2  13  1
# 12 14  4