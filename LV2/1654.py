import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = []
for i in range(n):
    d = int(input())
    arr.append(d)


def get_number_of_count(len_x):
    count = 0
    for i in arr:
        count += (i // len_x)
    
    return count

max_len = max(arr)
min_len = 1
real_val = False
# prev_mid = 0
# if n > 1:
#     while min_len <= max_len:
#         mid_len = (min_len + max_len) // 2
#         counts = get_number_of_count(mid_len)
#         # print("md", mid_len)
#         # print("ct", counts)
        

        
#         if counts < k:
#             max_len = mid_len -1
#             # prev_mid = mid_len
                
#         elif counts > k:
#             min_len = mid_len +1
#             # prev_mid = mid_len
            
#         else:
#             real_val = True
#             print(mid_len)
#             break
        
#     if real_val == False:
#         print(prev_mid)
# else:
#     print(arr[0])
# print(mid_len)

while min_len <= max_len:
        mid_len = (min_len + max_len) // 2
        counts = get_number_of_count(mid_len)
        # print("md", mid_len)
        # print("ct", counts)
        
        if counts < k:
            max_len = mid_len -1
            # prev_mid = mid_len
                
        else:
            min_len = mid_len +1
print(max_len)

