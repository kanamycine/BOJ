tc = int(input())
for t in range(1,tc+1):
    print('*'*t + ' '*(tc-t) +' '*(tc-t) + '*'*t )
for j in range(1, tc):
    print('*'*(tc-j) + ' '*(j) + ' '*(j) + '*'*(tc-j))