a, b = map(int, input().split())

def gcd(x, y):
    r = x % y
    if r == 0:
        return y
    return gcd(y, r)

def lcm(x, y):
    gcd_of_x_y = gcd(x, y)
    remainder_of_x = x // gcd_of_x_y
    remainder_of_y = y // gcd_of_x_y

    return gcd_of_x_y * remainder_of_x * remainder_of_y

print(gcd(a, b))
print(lcm(a, b))