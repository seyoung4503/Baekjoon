import sys
input = sys.stdin.readline

r = 31
M = 1234567891

n = int(input())
array = list(input())
array = array[:-1]

arr_num = [ord(i)-96 for i in array]

hashing = 0
for i in range(len(arr_num)):
    hashing += (arr_num[i] * (r**i))% M

hashing %= M
print(hashing)


