
"""
ID: renvanro1
LANG: PYTHON3
TASK: gift1
"""

file = open('gift1.in','r')
file = [line.strip() for line in file.read().splitlines()]

counter = int(file[0])+1
friends_group = {}
for i in range(1,counter):
    friends_group[file[i]] = 0

while counter < len(file):
    distributor = file[counter]
    counter += 1
    s = file[counter].split()
    sum = int(s[0])
    friend_to_distribute = int(s[1])
    counter += 1
    
    if friend_to_distribute == 0:
        friends_group[distributor] = friends_group[distributor] + sum
    else:
        sum_per_persona = sum//friend_to_distribute
        friends_group[distributor] = friends_group[distributor] + (sum%friend_to_distribute) - sum
        for i in range(counter,counter+friend_to_distribute):
            friends_group[file[counter]] = friends_group[file[counter]] + sum_per_persona
            counter += 1
        
fin = open('gift1.out','w')
for i in friends_group:
    fin.write(i+' '+str(friends_group[i])+'\n')
fin.close()
