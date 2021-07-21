n = int(input())
for i in range(n):
    str = input()
    left = []
    right = []
    for i in str:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)

    # tmp = left + (list(reversed(right)))
    # for i in tmp:
    #     print(i, end='')




    left.extend(reversed(right))
    print(''.join(left))