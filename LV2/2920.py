import sys
input = sys.stdin.readline

ascending = "1 2 3 4 5 6 7 8\n"
descending = "8 7 6 5 4 3 2 1\n"
line = input()
if line == ascending:
    print("ascending")
elif line == descending:
    print("descending")
else:
    print("mixed")
