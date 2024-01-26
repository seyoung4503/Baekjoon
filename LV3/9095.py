import sys
input = sys.stdin.readline

n = int(input())
dp = [1, 2, 4]
nums = []
for i in range(n):
    x = int(input())
    nums.append(x)

max_num = max(nums)

for i in range(3, max_num):
    dp.append(dp[i-3] + dp[i-2] + dp[i-1])



for i in nums:
    print(dp[i-1])

