n = int(input())
for i in range(n):
    A, B = list(input().split())
    a = int(A)
    for i in B:
        print(i * a, end='')
    print()