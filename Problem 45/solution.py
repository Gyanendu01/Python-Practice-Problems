# function to get dates from the user
def get_dates():
    date1 = input("\n\tEnter first date(day/month/year): ")
    date2 = input("\n\tEnter second date(day/month/year): ")
    
    date1 = date1.split("/")
    date1 = int(date1[0])
    
    date2 = date2.split("/")
    date2 = int(date2[0])

    return date1, date2

# function to find hours between two dates
def get_hours(d1,d2):
    if d1 == d2:
        print("\n\tNumber of hours between two dates: 24 Hours")
    if d1 > d2:
        print("\n\tNumber of hours between two dates: {}".format((d1-d2)*24))
    if d2 > d1:
        print("\n\tNumber of hours between two dates: {}".format((d2-d1)*24))

# main program
val = get_dates()
get_hours(val[0],val[1])
