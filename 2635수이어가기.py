n = int(input())

for i in range(1, n+2):
    lst = []
    lst = [n, i]
    j = 0
    while True :
        a = lst[j] - lst[j+1]
        if a < 0:
            break
        lst.append(a)
        j += 1
print(lst)