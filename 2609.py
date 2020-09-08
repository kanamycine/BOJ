def GCD(a, b):
    if (b == 0):
        return a
    else:
        return GCD(b, a % b)


a, b = map(int, input().split())
print(GCD(a, b))
print(a*b//GCD(a, b))
