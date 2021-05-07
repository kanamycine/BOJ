n = int(input())
for i in range(n):
    lst = list(map(int, input().split()))
    count = 0
    ans = 0
    for i in range(len(lst)):
        lst2 = lst[1:]
    sum_lst = sum(lst2)
    avr = sum_lst/len(lst2)
    for i in range(len(lst2)):
        if lst2[i] > avr:
            count += 1
    ans = (count/len(lst2))

    ans = ans * 100
    realans = round(ans, 3)
    print(str(realans)+'%')
