def mixed_fraction(s):
    a = ''
    b = ''
    d = False
    for i in s:
        if i == '/':
            d = True
        elif d == False and i != '/':
            a = a + i
        elif d == True and i != '/':
            b = b + i

    return a//b