import sys
input = sys.stdin.readline

n = int(input())
x = []
ans = []

for i in range(n):
    y = int(input())
    x.append(y)

x.sort()
arithmetic_mean = round(sum(x)/n)
#ans.append(round(sum(x)/n))
print(arithmetic_mean)

print(x[len(x)//2])

mode = {}
for i in x:
    if i in mode.keys():
        mode[i] += 1
    else:
        mode[i] = 1

mode_list = list(mode.items())
# print(mode)
# print(mode_list)
c = sorted(mode_list, key = lambda x : -x[1])
# print(c)
if len(c) > 1:
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
else:
    print(c[0][0])

ranges = x[-1] - x[0]
#ans.append(ranges)
print(ranges)