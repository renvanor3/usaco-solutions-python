"""
ID: renvano1
LANG: PYTHON3
TASK: transform
"""

with open('transform.in', 'r') as file:
    lines = file.read().strip()

lines = lines.split('\n')

n = int(lines[0])
before = lines[1:n+1]
after = lines[n+1:]

class Transformation:
    def __init__(self, before, after, tier):
        self.before = before
        self.after = after
        self.tier = tier
        self.n = 7
        t1 = self.t1(before)
        t2 = self.t1(t1)
        t3 = self.t1(t2)
        t4 = self.t4(t2)
        t4_1 = self.t1(t4)
        t4_2 = self.t1(t4_1)
        t4_3 = self.t1(t4_2)

        if t1 == after:
            self.n = 1
        elif t2 == after:
            self.n = 2
        elif t3 == after:
            self.n == 3
        elif t4 == after:
            self.n = 4
        elif t4_1 == after or t4_2 == after or t4_3 == after:
            self.n = 5
        elif before == after:
            self.n = 6       
                 
    def t1(self,before):
        unit = []
        for i in range(self.tier):
            unit.append(("".join([x[i] for x in before]))[::-1])
        return unit
    def t4(self, before):
        ref = self.tier // 2
        unit = []
        if self.tier % 2 == 0:
            unit += before[ref:][::-1]
            unit += before[:ref][::-1]
        else:
            unit += before[ref+1:][::-1]
            unit.append(before[ref])
            unit += before[:ref][::-1]

        return unit
    def __str__(self):
        return str(self.n)

objet = Transformation(before,after,n)    

fin = open('transform.out','w')
fin.write(str(objet.n)+'\n')
fin.close()



