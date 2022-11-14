import datetime as dt

now = dt.datetime.now()
year = now.year
day_of_weak = now.weekday()
print(now,"====" ,year, "====", day_of_weak)

date_of_birth = dt.datetime(year=1995, month=12, day=7,hour=5, minute=30)
print(date_of_birth)