"""
ID: renvanro1
LANG: PYTHON3
TASK: ride
"""
import string
alphabet = list(string.ascii_uppercase)


with open ('ride.in', 'r') as ride:
    comet = ride.readline()
    group = ride.readline()

pos_in = [[],[]]
for i in comet:
    if i in alphabet:
        pos_in[0].append(alphabet.index(i)+1)

for i in group:
    if i in alphabet:
        pos_in[1].append(alphabet.index(i)+1)

tf = []
for list in pos_in:
    a = 1
    for j in list:
        a = a * j
    tf.append(a%47)

fin = open('ride.out','w')
if tf[0] == tf[1]:
    fin.write('GO\n')
else:
    fin.write('STAY\n')

fin.close()