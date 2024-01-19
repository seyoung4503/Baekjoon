import sys
input = sys.stdin.readline

brakets = {")" : "(", "]" : "["}

while True:
    input_line = input()
    stack = []
    isBalance = True

    if input_line == ".\n":
        break

    for i in input_line:
        if i == "(" or i == "[":
            stack.append(i)
        if i == ")" or i == "]":
            if len(stack) == 0 or brakets[i] != stack[-1]:
                isBalance = False
                break
            stack.pop()
    if len(stack) != 0:
        isBalance = False
    if isBalance:
        print("yes")
    else:
        print("no")
