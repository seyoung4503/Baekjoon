import sys
input = sys.stdin.readline

n = int(input())

stair = [0]
for i in range(n):
    x = int(input())
    stair.append(x)


# dp_st = [0 for i in range(n+1)]
# visit  =[0 for i in range(n+1)] 

# dp_st[0] = 1
# visit[0] = 1

# ans = 0
# def climb(stair_num):
#     if visit[-1] == 1:
#         # print(dp_st)
#         global ans
#         if ans < sum(dp_st):
#             ans = sum(dp_st)
#         return

#     for i in range(stair_num, n):
#         # print("visit ", visit, i)
#         if visit[i] == 1 and visit[i-1] == 1:
#             continue
#         # elif i != 0 and visit[i] == 0 and visit[i-1] == 0:
#         #     continue
#         else:
#             dp_st[i+1] = stair[i+1]
#             visit[i+1] = 1
#             climb(i+1)
#             dp_st[i+1] = 0
#             visit[i+1] = 0

#         # print("dp ", dp_st)
            

# climb(0)
# print(ans)

stair = stair[1:]
# print(stair)
dp = []
if n > 2:
    dp.append(stair[0])
    dp.append(stair[0] + stair[1])
    dp.append(max(stair[0]+stair[2], stair[1]+stair[2]))

    # dp[4] = (10 + 20) + 25 or 10 + 15+ 25
    for i in range(3, n):
        x = dp[i-2]
        y = dp[i-3] + stair[i-1]
        dp.append(max(x, y) + stair[i])
else:
    dp.append(sum(stair))

print(dp[-1])

# print(dp)
