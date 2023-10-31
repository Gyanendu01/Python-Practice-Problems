# function to get dates from the user
def get_dates():
    date1 = input("\n\tEnter first date(day/month/year): ")
    date2 = input("\n\tEnter second date(day/month/year): ")
    
    date1 = date1.split("/")
    date1 = int(date1[0])
    
    date1 = date1.split("/")
    date1 = int(date1[0])
    