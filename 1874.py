import sys
n = int(input())
a = [int(input()) for _ in range(n)]
print(a)
stack = []
m = 0
ans = []

for x in a :
    if x > m:
        while x > m:
            m += 1
            stack.append(m)
            ans += ['+']
        stack.pop()
        ans += ['-']
    else :
        if stack[-1] != x:
            print('NO')
            sys.exit(0)
        stack.pop()
        ans += ['-']
print('\n'.join(ans)+'\n')