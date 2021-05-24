# str = input()
# count = 0
# lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# for i in range(len(lst)):
#     if lst[i] in str:
#         croa = str.find(lst[i])
#         del str[croa:len(lst[i])]
#         count += 1
# print(str)

# res = len(str) + count
# print(res)

# 나의 풀이

# 두번째 풀이
str = input()
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in range(len(lst)):
    if lst[i] in str:
        str = str.replace(lst[i], "0")
res = len(str)
print(res)
