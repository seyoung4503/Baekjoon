import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    sub_arr = list(map(int, input().split()))
    arr.append(sub_arr)

def isBlueOrWhite(r, c, n):
    free = []
    for i in range(n):
        sum_of_line = sum(arr[r+i][c:c+n])

        free.append(sum_of_line) 

    
    sum_of_free = sum(free)
    if sum_of_free == n*n:
        return 1
    if sum_of_free == 0:
        return 0
    else:
        return -1
    
    
    
num_of_colors = [0, 0] # white, blue
def recursion(r, c, n):
    color = isBlueOrWhite(r, c, n)
    if color != -1:
        num_of_colors[color] += 1
        return
    
    n //= 2
    recursion(r, c, n)
    recursion(r + n, c, n)
    recursion(r, c+n, n)
    recursion(r+n, c+n, n)
    n *= 2


recursion(0, 0, n)
for i in num_of_colors:
    print(i)

