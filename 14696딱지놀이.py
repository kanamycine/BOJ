n = int(input())
for i in range(n):
    lstf = list(map(int, input().split()))
    lstl = list(map(int, input().split()))
    lstf = lstf[1:]
    lstl = lstl[1:]
    lstf4c = lstf.count(4)
    lstl4c = lstl.count(4)
    lstf3c = lstf.count(3)
    lstl3c = lstl.count(3)
    lstf2c = lstf.count(2)
    lstl2c = lstl.count(2)
    lstf1c = lstf.count(1)
    lstl1c = lstl.count(1)

    if lstf4c > lstl4c:
        print('A')
    elif (lstf4c == 0 and lstl4c == 0) or lstf4c == lstl4c:
        if lstf3c > lstl3c:
            print('A')
        elif (lstf3c == 0 and lstl3c == 0) or lstf3c == lstl3c:
            if lstf2c > lstl2c:
                print('A')
            elif (lstf2c == 0 and lstl2c == 0) or lstf2c == lstl2c:
                if lstf1c > lstl1c:
                    print('A')
                elif lstf1c == lstl1c:
                    print('D')
                else:
                    print('B')
            else:
                print('B')
        else:
            print('B')
    else:
        print('B')
