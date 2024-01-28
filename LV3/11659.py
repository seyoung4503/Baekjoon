import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr_sum = [0 for i in range(len(arr))]
arr_sum[0] = arr[0]
for i in range(1, len(arr)):
    arr_sum[i] = arr_sum[i-1] + arr[i]

# print(arr_sum)


for k in range(m):
    i, j = map(int, input().split())
    i -= 1

    if i == 0:
        print(arr_sum[j-1])
    else:
        print(arr_sum[j-1] - arr_sum[i-1])

