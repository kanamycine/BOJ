n = int(input())
lst = [0 for _ in range(21)]
for i in range(2, 21):
    lst[0] = 0
    lst[1] = 1
    lst[i] = lst[i-1] + lst[i-2]
print(lst[n])#