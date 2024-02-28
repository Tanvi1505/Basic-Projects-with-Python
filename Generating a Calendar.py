import calendar
y = int(input("enter the year: "))
Cal = calendar.TextCalendar(calendar.SUNDAY)

i=1
while i<=12:
    Cal.prmonth(y,i)
    i+=1
    



