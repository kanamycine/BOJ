import sys
N = int(sys.stdin.readline())
# N = int(input())
for _ in range(N):
    ps_count = 0
    ps_check = False
#     line = input()
    line = sys.stdin.readline().rstrip()
    for char in line:
        if char == '(':
            ps_count += 1
        elif char == ')':
            if ps_count == 0:
                print('NO')
                ps_check = True
                break
            ps_count -= 1
    if not ps_check:
        if ps_count == 0:
            print('YES')
        else:
            print('NO')