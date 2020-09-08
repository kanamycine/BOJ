def GCD(a, b):
    if (b == 0):
        return a
    else:
        return GCD(b, a % b)


tc = int(input())
for t in range(1, tc + 1):
    a, b = map(int, input().split())
    print(a*b//GCD(a, b))
