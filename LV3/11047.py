import sys
input = sys.stdin.readline

n, k = map(int, input().split())

value = []
for i in range(n):
    x = input()
    x = x[:-1]
    x = int(x)
    value.append(x)

coin = 0
remain = k
for i in reversed(range(len(value))):

    # print(value[i])
    if remain == 0:
        break

    curVal = value[i]
    while curVal <= remain:
        coin += remain // curVal
        remain %= curVal

    # print(remain)




print(coin)