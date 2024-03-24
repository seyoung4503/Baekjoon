import sys
from collections import deque
input = sys.stdin.readline

eqation = input()

formula = []
number = ''
for i in eqation:
    
    if i >= '0' and i <= '9':
        number += i
    else:
        formula.append(str(int(number)))
        formula.append(i)
        number = ''

formula = formula[:-1]
# print(formula)

strings = ''
minus = 0
isNegative = False
j = 0
for i in formula:
    if i == '-' and isNegative == False:
        strings += i
        strings += '('
        minus += 1
        isNegative = True
        # if j != 0 and formula[j-1] == '-'
    
    elif i == '-' and isNegative == True:
        strings += ')'
        strings += i
        strings += '('
        
        # minus -= 1
        # isNegative = False

    else:
        strings += i
        # isNegative = False
    j += 1


if minus > 0:
    for i in range(minus):
        strings += ')'
# print(strings)
print(eval(strings))