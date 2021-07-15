while(True):
    s = input()
    if s == '0':
        break
    result = 'yes'
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            result = 'no'
            break
    print(result)
