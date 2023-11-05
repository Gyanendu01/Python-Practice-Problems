# function to get input from user
def usr_input():
    num = int(input("\n\tEnter a number: "))
    percentage = int(input("\tEnter The percentage: "))
    return num, percentage

# function to calculate percentage
def cal_percentage(num,perc):
    print("\n\t{}% of {} is {}".format(perc,num,(perc/100)*num))

# main program
val = usr_input()
cal_percentage(val[0],val[1])