n = int(input())
for i in range(n):
    A,B = map(str, input().split())
    Alst = sorted(list(A))
    Blst = sorted(list(B))
    result = ''
    if Alst == Blst:
        print('Possible')
    else:
        print('Impossible')


    