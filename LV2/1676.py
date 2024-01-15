import sys
import math
input = sys.stdin.readline

n = int(input())

num = math.factorial(n)
print(num)
count = 0
while num % 10 == 0:
    count += 1
    num //= 10
print(count)

# arr = [0, 0, 0]
count_5 = 0
for i in range(1, n+1):
    buf_5 = i
    while buf_5 % 5 == 0:
        print("fsdfs", buf_5)
        print()
        buf_5 //= 5 
        count_5 += 1

    
print(count_5)
    