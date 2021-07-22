# arr = []
# for i in range(28):
#     arr.append(int(input()))
# print(arr)
# x = sorted(arr)
# print(x)
# oops = []
# for i in (1, 30):
#     if i not in x:
#         oops.append(i)
# print(oops)
# for j in oops:
#     print(j)

chk = [0] * 31
for i in range(28):
    chk[int(input())] += 1
for j in range(1, 31):
    if not chk[j]:
        print(j)