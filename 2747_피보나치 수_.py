# n = int(input())

# def fib(n):
#     if n == 0 :
#         return 0
#     elif n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)

# print(fib(n))
n = int(input())
arr = [0, 1]
for i in range(2, n):
    arr.append(arr[-1]+arr[-2])
print(arr[-1]+arr[-2])