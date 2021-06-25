# n = int(input())
# arr = []
# for j in range(n):
#     num, str = input().split()
#     res = ''
#     for i in str:
#         res += int(num) * i
#     arr.append(res)
# for i in arr:
#     print(i)

t = int(input())
for i in range(t):
    num, str = input().split()
    res = ''
    for i in str:
        res += int(num) * i
    print(res)
