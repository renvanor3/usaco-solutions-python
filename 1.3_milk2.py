"""
ID: renvano1
LANG: PYTHON3
TASK: milk2
"""

l = []
with open('milk2.in','r') as fp:
    cmd = fp.readlines()
    for i in cmd:
        l.append(i.strip())

start = int(l[0])
del l[0]
def time(s):
    for i in range(len(s)):
        s[i] = s[i].split()
        for j in range(len(s[i])):
            s[i][j] = int(s[i][j])
    return s
time(l)
l.sort(key=lambda lst:lst[0])

def order(l):
    lf = []
    pro = l[0][1]
    anta = l[0][0]
    for i in range(len(l)):
        if pro >= l[i][1]:
            if i == len(l)-1:
                lf.append([anta,pro])
            else:
                continue
        elif pro >= l[i][0]:
            if i == len(l)-1:
                lf.append([anta,l[i][1]])
            else:
                pro = l[i][1]
        else:
            lf.append([anta,pro])
            pro = l[i][1]
            anta = l[i][0]
            if i == len(l)-1:
                lf.append([l[i][0],l[i][1]])
    return lf


def most(t):
    most = t[0][1] - t[0][0]
    for i in t:
        a = i[1] - i[0]
        if a > most:
            most = a
    return str(most)

def less(t):
    if len(t) == 1:
        return str(0)
    idle = t[1][0] - t[0][1]
    for i in range(1,len(t)):
        a = t[i][0] - t[i-1][1]
        if a >= idle:
            idle = a

    return str(idle)

final = most(order(l)) + ' ' + less(order(l)) + '\n'

with open('milk2.out','w') as ft:
    ft.write(final)