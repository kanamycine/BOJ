t = int(input())
for tc in range(1, t+1):
    lst = list(map(str, input().split()))
    lst.reverse()
    tmp = ''
    for i in lst:
        tmp += i + ' '
    print('Case #{}: {}'.format(tc, tmp))
