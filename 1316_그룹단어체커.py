#str = input()
# for i in str:
#    if str[str.index(i)+1] == i:
#        str[str.index(i)] = '0'

# print(str)

n = int(input())
count = 0
for i in range(n):

    lst = list(input())
    lst.append("")
    for i in range(len(lst) - 1):
        if lst[i] == lst[i+1]:
            lst[i] = 0
    remove_set = {0, ''}
    res = [i for i in lst if i not in remove_set]

    if len(res) == len(set(res)):
        count += 1
print(count)
