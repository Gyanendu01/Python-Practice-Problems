# function to get input from user
def usr_input():
    num = int(input("\n\tEnter a number: "))
    while True:
        percentage = int(input("\tEnter The percentage: "))
        if percentage >0 and percentage <=100:
            break
        else:
            print("\n\tplease enter a number between 0 and 100")
    return num, percentage

# function to calculate percentage
def cal_percentage(num,perc):
    print("\n\t{}% of {} is {}".format(perc,num,(perc/100)*num))

# main program
val = usr_input()
cal_percentage(val[0],val[1])

while True:
    while True:
        condn = input("\n\tDo you want to continue (y/n): ")
        condn = condn.lower()
        if condn in ['y', 'n']:
            break
    if condn == 'y':
        val = usr_input()
        cal_percentage(val[0],val[1])
    else:
        print("\n\tThank You")
        break