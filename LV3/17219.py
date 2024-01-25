import sys
input = sys.stdin.readline

n, m = map(int, input().split())

site = {}
for i in range(n):
    address, password = input().split()
    site[address] = password


for i in range(m):
    address = input()
    address = address[:-1]
    print(site[address])
# print(site)