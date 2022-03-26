import datetime as dt

now = dt.datetime.now()
#makes an object called now of class datetime
year = now.year
#which has properties like year which we can access
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1994, month=6, day=29, hour=9, minute=35)
print(date_of_birth)