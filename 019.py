import datetime

count = 0
for year in xrange(1901, 2001):
    for month in xrange(1, 13):
        d = datetime.date(year, month, 1)
        if d.weekday() == 6:
            count += 1

print count
