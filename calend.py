import calendar
#janaray to december
i=1
year = int(input("enter the year "))
while i<=12:
    print(calendar.month(year,i))
    i+=1


#december to janaray
i=12
year = int(input("enter the value "))
while i>=1:
    print(calendar.month(year,i))
    i-=1
