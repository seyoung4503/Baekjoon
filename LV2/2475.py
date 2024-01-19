import sys
input = sys.stdin.readline

num = list(map(int, input().split()))

x = sum([i*i%10 for i in num])%10
print(x)