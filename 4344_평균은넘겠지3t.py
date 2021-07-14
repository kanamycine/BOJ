n = int(input())
for i in range(n):
    lst = list(map(int, input().split()))
    total = 0
    for j in lst:
        total += j
    total = total - lst[0]
    top = []
    avg = total/lst[0]
    student_num = lst[0]
    lst[0] = 0
    for k in lst:
        if avg < k:
            top.append(k)
    count = len(top) / student_num
    print("{:.3f}%".format(count * 100))

    
