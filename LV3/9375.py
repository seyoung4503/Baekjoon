import sys
from itertools import combinations
input = sys.stdin.readline

t = int(input())
closet = {}
for i in range(t):
    closet.clear()
    n = int(input())

    
    for i in range(n):
        
        name, type_ = input().split()
        if type_ in closet.keys():
            closet[type_] += 1
        else:
            closet[type_] = 1

    values = [i+1 for i in closet.values()]

    val = 1
    for i in values:
        val *= i
    
    print(val-1)

    # print(closet)

    # sums = sum(closet.values())

    # keys = closet.keys()
    # for i in range(2, len(keys)+1):
    #     comb = list(combinations(keys, i))
    #     # print(comb)
    #     val = 1
    #     for j in range(len(comb)):
            
    #         # fashion_type = comb[j]
    #         for types in comb[j]:
    #             k = closet[types]
    #             val *= k
        
    #     sums += val
    
    # print(sums)
            
    


# a : 1 2 3
# b : 4 5
# c : 6

# a + b + c + a*b + b*c + c*a + a*b*c = (a + 1)(b + 1)(c + 1) -1

# 1개 선택하는 경우
# 2개 선택하는 경우
# ...
# n개 선택하는 경우 나눠서 계산
    
