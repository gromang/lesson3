from datetime import date, datetime, timedelta

dt = date.today()
yesterday = dt - timedelta(days=1)
tommorow = dt + timedelta(days=1)
previous_month = dt.replace(month=int(dt.month - 1))

new_dt = '01/01/17 12:10:03.234567'
new_dt = datetime.strptime(new_dt, '%d/%m/%y %H:%M:%S.%f')

print(dt)
print(yesterday)
print(tommorow)
print(previous_month)
print(new_dt)
