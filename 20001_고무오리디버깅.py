s = input()
stk = []
while True:
    rubber = input()
    if rubber == "문제":
        stk.append(1)
    elif rubber == "고무오리":
        if stk: 
            stk.pop()
        else:
            stk.append(1)
            stk.append(1)
    elif rubber == "고무오리 디버깅 끝":
        break
if len(stk) == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")