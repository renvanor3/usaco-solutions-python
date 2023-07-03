"""
ID: renvano1
LANG: PYTHON3
TASK: ride
"""
import string
alphabet = list(string.ascii_uppercase)


with open ('ride.in', 'r') as ride:
    comet = ride.readline()
    group = ride.readline()

sa = 0
for i in comet:
    sa *= (alphabet.index(i)+1)
sb = 0
for i in group:
    sb *= (alphabet.index(i)+1)
    
fin = open('ride.out','w')
if sa%47 == sb%47:
    fin.write('GO\n')
else:
    fin.write('STAY\n')

fin.close()