import sys
import math
input = sys.stdin.readline

stack = []
push_pop = []
n = int(input())

stack_num = 1
for i in range(n):
    
    if len(stack) != 0 and stack[-1] == x:
        push_pop.append("-")
        stack.pop()
    
    x = int(input())

    temp = stack_num

    for j in range(temp, x+1):
        stack.append(j)
        push_pop.append("+")
        stack_num += 1
    

if len(stack) == 1:
    push_pop.append("-")
    for i in push_pop:
        print(i)
else:
    print("NO")