import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

arr.sort()

# print(arr)

sums = [arr[0]]
for i in range(1, n):
    sums.append(sums[i-1] + arr[i])

print(sum(sums))