import sys
from collections import Counter
input = sys.stdin.readline

EPS = 1e-9

N, M, B = map(int, input().split())
cord = []

for i in range(N):
    cord.append(list(map(int, input().split())))

maxheight = -1
mintime = 1e9

for height in range(257):
    remove_ctr = 0
    mount_ctr = 0

    for i in range(N):
        for j in range(M):
            height_ij = cord[i][j] - height

            if height_ij < 0:
                mount_ctr -= height_ij
            else:
                remove_ctr += height_ij
        
    if remove_ctr + B >= mount_ctr:
        time = 2* remove_ctr + 1* mount_ctr

        if mintime >= time:
            mintime = time
            maxheight = height

print(mintime, maxheight)