import sys
input = sys.stdin.readline

s = [0 for i in range(21)]

def calcualte(order):

    if len(order) == 2:
        attr = int(order[1])
    command = order[0]

    if command == 'add':
        s[attr] = 1
    elif command == 'remove':
        s[attr] = 0
    elif command == 'check':
        print(s[attr])
    elif command == 'toggle':
        if s[attr] == 1:
            s[attr] = 0
        else:
            s[attr] = 1
    elif command == 'all':
        for i in range(21):
            s[i] = 1
    
    elif command == 'empty':
        for i in range(21):
            s[i] = 0

    

m = int(input())

for i in range(m):
    cmd = input().split()

    calcualte(cmd)

    # print(cmd)
