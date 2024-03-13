import sys
input = sys.stdin.readline

channel_n = int(input())

broken_button_n = int(input())
broken_buttons = []
if broken_button_n != 0:
    broken_buttons = list(map(int, input().split()))
# print(broken_buttons)

maximum_pressed = abs(channel_n - 100)

nums_min = maximum_pressed

# count = 0
for i in range(1000001):
    for j in range(len(str(i))):
        if int(str(i)[j]) in broken_buttons:
            break
        elif j == len(str(i)) - 1:
            nums_min = min(len(str(i)) + abs(i - channel_n), nums_min)

print(nums_min)