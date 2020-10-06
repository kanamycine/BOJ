import sys
n = sys.stdin.readline().rstrip()
b = int(sys.stdin.readline())
left = list(n)
right = []

for i in range(b):
    C = sys.stdin.readline().rstrip()
    if C == 'L' and left:
            right.append(left.pop())
    elif C == 'D' and right:
            left.append(right.pop())
    elif C == 'B' and left:
            left.pop()
    else:
        if C[0] == 'P':
            left.append(C[2])
    
    
left += right[::-1]
print(''.join(left))  
#  

