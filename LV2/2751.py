import sys
input = sys.stdin.readline
printf = sys.stdout.write
n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)



arr.sort()

for i in range(n):
    printf(str(arr[i]))
    print()