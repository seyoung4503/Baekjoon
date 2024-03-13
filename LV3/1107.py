import sys
input = sys.stdin.readline

channel_n = int(input())

broken_button_n = int(input())

broken_buttons = list(map(int, input().split()))

maximum_pressed = abs(channel_n - 100)

nums = [(channel_n % (10^i)) for i in range(len(str(channel_n))+1, 1)]

print(nums)