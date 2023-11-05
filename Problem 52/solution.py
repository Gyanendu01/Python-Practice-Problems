# function to accept user input
def usr_input():
    print("\n\tEnter the elements separated by spaces.....")
    usr_val = [float(x) for x in input().split()]
    print("\n\tEntered elements are: {}".format(usr_val))
    return usr_val

# function to calculate the average and display the result
def usr_average(val):
    sum = 0
    for i in val:
        sum = sum+i
    avg = sum/len(val)
    print("\n\tAverage: {}".format(avg))

# main program
usr_val = usr_input()
usr_average(usr_val)