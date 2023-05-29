"""
ID: renvano1
LANG: PYTHON3
TASK: friday
"""

with open('friday.in','r') as fp:
    end_year = int(fp.readline()) + 1900

month_days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
week_days = {6:0,0:0,1:0,2:0,3:0,4:0,5:0}
def leap_year(n):
    if n%4 == 0 and (n%100 == 0 and n%400 != 0) == False:
        return 29
    else:
        return 28

year = 1900
month = 1
day = 1
week_day = 1

while year < end_year:
    month_days[2] = leap_year(year)
    if month == 12 and day == 31:
        year += 1
        month = 1
        day = 1
    elif day == month_days[month]:
        day = 1
        month += 1
    else:
        day += 1
    week_day += 1
    if day == 13:
        week_days[week_day%7] += 1

fin = ' '.join(str(week_days[i]) for i in week_days)
end = open('friday.out','w')
end.write(fin + '\n')
end.close()