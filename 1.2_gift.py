"""
ID: renvanro1
LANG: PYTHON3
TASK: gift1
"""


file = open('gift1.in','r')
file = file.read().splitlines()

friends_group_name = {}
start = int(file[0])+1
for i in range(1,start):
    friends_group_name[file[i]] = 0

long = len(file)
while start < long and (long - start) > 2:
    distributor = file[start]
    s = file[start+1].split()
    sum = int(s[0])
    friend_to_ditribute = int(s[1])
    if friend_to_ditribute == 0:
        friends_group_name[distributor]= friends_group_name[distributor] + sum
        start += 2
        continue
    else:
        sum_per_persona = sum//friend_to_ditribute
        for i in range(start+2,start+2+friend_to_ditribute):
            friends_group_name[file[i]] = friends_group_name[file[i]] + sum_per_persona
            friends_group_name[distributor] = friends_group_name[distributor] - sum_per_persona
        start = i + 1

fin = open('gift1.out','w')
for i in friends_group_name:
    fin.write(i+' '+str(friends_group_name[i])+'\n')
fin.close()
