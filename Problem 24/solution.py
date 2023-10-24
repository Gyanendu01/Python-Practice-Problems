# Function to take input from the user
def usr_input():
    
    num = int(input("\tEnter a number: "))
    return num

# Function to check whether the input is odd or even
def check_input(num):
    if num %2 == 0:
        print("\n\tProvided number({}) is even".format(num))
    else:
        print("\n\tProvided number({}) is odd".format(num))

# Main program
val = usr_input()
check_input(val)