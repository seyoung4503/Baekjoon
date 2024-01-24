import sys
input = sys.stdin.readline

n, m = map(int, input().split())

Pookyman = {}
inv = {}
for i in range(n):
    x = input()
    Pookyman[x[:-1]] = i + 1
    # inv[i+1] = x[:-1]
inv = {v:k for k, v in Pookyman.items()}
# inv = dict(zip(Pookyman.values(), Pookyman.keys()))
# Pookyman = []
# for i in range(n):
#     x = input()
#     Pookyman.append(x[:-1])


# print(Pookyman)
# print(inv)
for i in range(m):
    x = input()
    x = x[:-1]
    if x.isdigit():
        # print(x)
        x = int(x)

        print(inv[x])
        

    # Problem.append(x)
    else:
        print(Pookyman[x])


# print(Pookyman)
# print(Pookyman_List)
# print(Problem)




