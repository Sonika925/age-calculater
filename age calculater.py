from datetime import date
def agecal(y,m,d):
    today=date.today()
    dob=date(y,m,d)
    age=date(today-dob).days/365
    print(int(age))
agecal(2002,11,9)
