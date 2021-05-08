str = input()
lst = [-1 for i in range(26)]
cnt = 0
for i in str:
    if lst[ord(i)-97] == -1:
        lst[ord(i)-97] = cnt
        cnt += 1
    else:
        cnt += 1


for i in range(26):
    print(lst[i], end=" ")
