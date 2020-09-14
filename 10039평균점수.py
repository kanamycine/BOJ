lst = []
for i in range(5):
    n = int(input())

    if n <= 40:
        lst.append(40)

    else:
        lst.append(n)
print(sum(lst)//5)
