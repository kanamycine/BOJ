string, tmp, result = input(), '', ''

tag = False

for i in string:
    if i == '<':
        tag = True
        result += tmp[::-1] + "<"
        tmp = ''
    elif i == '>':
        tag = False
        result += '>'
    elif i == ' ':
        if tag:
            result += ' '
        else:
            result += tmp[::-1] + ' '
            tmp = ''
    else:
        if tag:
            result += i
        else:
            tmp += i
result += tmp[::-1]

print(result)
