import sys
input = sys.stdin.readline

EPS = 1e-9
n = int(input())

diff = []
for i in range(n):
    diff.append(int(input()))

diff.sort()

x = round(n * 0.15+EPS)


diff = diff[x:(n-x)]
# print(diff)
yes = sum(diff)

if n != 0:
    print(round(yes/(n - x*2) + EPS))
else:
    print(0)

# Idiv = 0
# for i in range(x):
#     yes -= diff[i]
#     yes -= diff[n-i-1]

#     Idiv += 2



# if n != 0:
#     div = n - Idiv
#     print(round(yes/div))
# else:
#     print(0)