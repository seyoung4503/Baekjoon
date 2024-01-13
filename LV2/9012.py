n = int(input())

def find_ps(ps):
    flag = 1
    sum_of_ps = 0
    for i in range(len(ps)):
        if ps[i] == "(":
            sum_of_ps += 1
        elif ps[i] == ")":
            sum_of_ps -= 1
        
        if sum_of_ps < 0:
            # print("NO")
            flag = 0
            break
    if sum_of_ps != 0:
        flag = 0
    return flag


i = 0
while n > i:
    ps = input()
    flag = find_ps(ps)
    # print("YES")
    if flag:
        print("YES")
    else:
        print("NO")

    i += 1