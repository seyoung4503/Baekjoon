import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

array = [[0 for i in range(2)] for j in range(2)]

# for i in range(len(array)):
#     print(array[i])

# 종료 조건
# 여는 수식
# 재귀 호출
# 닫는 수식
num_of_z = len(array)/2
temp = 0
# array[0][0] = 0
# array[0][1] = 1
# array[1][0] = 2
# array[1][1] = 3


def z(n, r, c, temp):
    if n == 0:
        return temp
    
    temp_X, temp_Y = 0, 0

    if r%2 != 0:
        temp_X = 2
    if c %2 != 0:
        temp_Y = 1 

    r //=2
    c //=2
    t = z(n-1, r, c, temp)
    # temp = 4 * t + temp_X + temp_Y

    return 4 * t + temp_X + temp_Y

print(z(N, r, c, temp))
    

