

def palindome(x):
    len_of_x = len(x)
    flag = "yes"
    if len_of_x == 1:
        flag = "yes"
    else :
        for i in range(len_of_x // 2):
            if x[i] != x[len_of_x - i-1]:
                flag = "no"
    print(flag)
    return

while True:
    inputs = input()
    if inputs[0] == "0":
        break
    palindome(inputs)