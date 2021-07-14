n = int(input())
for i in range(n):
    str = input()
    c, count = 0, 0
    for j in str:
        if j == 'O':
            c += 1
            count += c
        else:
            c = 0
    print(count)
