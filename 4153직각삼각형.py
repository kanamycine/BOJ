while(True):
    a = list(map(int, input().split()))
    m_num = max(a)
    if sum(a) == 0 :
        break
    a.remove(m_num)
    if a[0] ** 2 + a[1] ** 2 == m_num ** 2:
        print('right')
    else:
        print('wrong')