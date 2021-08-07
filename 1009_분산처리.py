n = int(input())

for i in range(n) :
    A, B = map(int,input().split())
    print(str(A ** B)[-1])##