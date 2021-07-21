n = int(input())
for i in range(n):
    str = input()
    left = []
    right = []
    for j in str:
        if j == '<':
            if len(left) != 0:
                right += left[-1]
                del left[-1]
            else : continue
        elif j == '>':
            if len(right) != 0:
                left += [right[0]]
                del right[0]
            else : continue   
        elif j == '-':
            if left[-1] != '':
                del left[-1]
            else : continue
        else:
            left += j

    print(''.join(left))
