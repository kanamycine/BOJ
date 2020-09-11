n = int(input())
max_l = 0
max_lst = []
for i in range(n+1):
    result = [n, i]
    j = 0
    while True:
        a = result[j] - result[j+1]
        if a <= -1:
            break
        result.append(a)
        if max_l < len(result):
            max_l = len(result)
            max_lst = result[:]
        j += 1
print(max_l)
for i in max_lst:
    print(i , end= " ")