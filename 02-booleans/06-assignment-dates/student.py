# write your code here
def is_valid_month(month):
    if 1<=month<=12:
        valid_month= True
    else:
        valid_month= False
    return valid_month

def is_leap_year(year):
    leap_year = False
    if year%4==0:
        if year%100!=0:
            leap_year=True
        elif year%100==0 and year%400==0:
            leap_year=True
    return leap_year

def has_30_days(month):
    valid_month= is_valid_month(month)
    month_of_30 = (month==4) or (month==6) or (month==9) or (month==11)
    valid_30= month_of_30==True and valid_month
    return valid_30

def has_31_days(month):
    valid_month= is_valid_month(month)
    month_of_31 = (month==1) or (month==3) or (month==5) or (month==7) or (month==8) or (month==10) or (month==12)
    valid_31= month_of_31==True and valid_month
    return valid_31

def has_28_days(month, year):
    leap_year= is_leap_year(year)
    if month==2 and leap_year==False:
        return True
    else:
        return False

def has_29_days(month, year):
    leap_year= is_leap_year(year)
    if month==2 and leap_year==True:
            return True
    else:
        return False

def is_valid_date(day, month, year):
    days_28=has_28_days(month,year) and day <=28
    days_29=has_29_days(month,year) and day <=29
    days_30=has_30_days(month) and day <=30
    days_31=has_31_days(month) and day <=31
    date_valid= days_28 or days_30 or days_31 or days_29
    return date_valid