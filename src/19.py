import datetime

def solve():
    i = 0
    for year in range(1901,2001):
        for month in range(1,13):
            if datetime.date(year,month,1).weekday() == 6:
                i = i + 1
    return i

print solve()
