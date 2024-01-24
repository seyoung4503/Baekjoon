import sys
input = sys.stdin.readline

n, m = map(int, input().split())

unheard = []
unsaw = []

for i in range(n):
    x = input()
    unheard.append(x[:-1])

for i in range(m):
    x = input()
    unsaw.append(x[:-1])

unheardof = list(set(unheard) & set(unsaw))
unheardof.sort()

print(len(unheardof))

for i in unheardof:
    print(i)