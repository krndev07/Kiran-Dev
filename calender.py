import datetime
def cal(y,m,d):
       x=datetime.datetime(y,m,d)
       print(x.strftime("%m"))
y=int(input("enter the year: "))
m=int(input("enter the month: "))
d=int(input("enter the date: "))
cal(y,m,d)