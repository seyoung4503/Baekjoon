import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

array = [[0 for i in range(2 ** N)] for j in range(2 ** N)]

for i in range(len(array)):
    print(array[i])

cnt = 0
row, col = 0, 0
def loop(n):
    
    
    if n == 1:
        array[row][col] == cnt
        array[row][col+1] == (cnt+1)
        array[row+1][col] == (cnt+2)
        array[row+1][col+1] == (cnt+3)
        cnt += 4
    if n > 1:
        n -= 1
        loop(n)
        n += 1
        




print(array[r][c])