#Topic ----

import time
seconds = time.time()
print(seconds)

#%%%
minutes = seconds / 60
print(minutes)

#%%%
hours = minutes / 60
print(hours)


#%%%
days = hours / 24
print(days)

#%%%
years = days / 365.25
print(years)

#%%%%
t = "1:12:23"
(h, m, s) = t.split(':')
result = int(h) * 3600 + int(m) * 60 + int(s)
result


#%%%
import datetime
hhmmss = '02:29:14'
[hours, minutes, seconds] = [int(x) for x in hhmmss.split(':')]
x = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
x
#datetime.timedelta(0, 8954)
x.seconds

#%%%
#If you actually wanted a Decimal

import decimal
decimal.Decimal(x.seconds)

#%%%
t = datetime.time(12,31,53)
ts = t.hour * 3600 + t.minute * 60 + t.second
print(ts)



#%%%%
#https://sumangangopadhyay.wordpress.com/2014/10/05/python-program-to-convert-hours-given-in-decimal-format-into-hours-minutes/
#https://www.w3resource.com/python-exercises/python-basic-exercise-65.php
