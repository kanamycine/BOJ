t = int(input())
for i in range(t):
    num, str = input().split()
    res = ''
    for i in str:
        res += int(num) * i
    print(res)
