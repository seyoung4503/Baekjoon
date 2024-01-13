n = int(input())
n_list = {}
# m_list = {}
ans = []
nums = input().split()
# print(nums)
for i in range(n):
    if nums[i] not in n_list:
        n_list[nums[i]] = 1
    else:
        n_list[nums[i]] += 1
# print(n_list)

m = int(input())
nums_m = input().split()

for i in range(m):
    if nums_m[i] in n_list:
        ans.append(n_list[nums_m[i]])
    else:
        ans.append(0)

for i in range(len(ans)):
    print(ans[i], end=' ')
print()