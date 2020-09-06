import sys
lines = sys.stdin.readlines()
for line in lines[:-1]:
    stack = []
    for i in line:
        if i == '(':
            stack.append(i)
        if i == '[':
            stack.append(i)

        if i == ')':
            if stack.pop() == '(':
                print('yes')
            else:
                print('no')
        if i == ']':
            if stack.pop() == '[':
                print('yes')
            else:
                print('no')
    if len(stack) == 0:
        print('yes')
