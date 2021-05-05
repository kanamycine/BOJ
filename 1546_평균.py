n = int(input())
lst = list(map(int, input().split()))

nummax = max(lst)
numsum = 0
for i in range(len(lst)):
    lst[i] = (lst[i]/nummax)*100
    numsum += lst[i]

print(numsum/n)
