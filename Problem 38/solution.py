# function to accpet input from the user
def usr_input():
    begin_val = int(input("\tEnter the start term value: "))
    end_val = int(input("\tEnter the end term value: "))
    return begin_val, end_val

# function to display the the terms along with the sum
def disp_term(begin_val,end_val):
    sum = 0
    print("\n\tNUMBER\t\tSUM")
    for i in range(begin_val, end_val+1):
        sum = sum+i
        print("\t{}\t\t{}".format(i, sum))

# Main program
val = usr_input()
disp_term(val[0],val[1])