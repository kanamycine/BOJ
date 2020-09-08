n = int(input())
def prime(n):
    if n < 2:
        return False
    for i in range(2, n+1):
        if i*i > n:
            if i % n == 0:
                return False
            else:
                return True

print(prime(n))
