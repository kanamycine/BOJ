n = int(input())
def prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n+1):
            if n % i == 0:
                return False
            else:
                return True
    
print(prime(n))