# Function to get two numbers from the user
def usr_input():
    num1 = int(input("\n\tEnter a number: "))
    num2 = int(input("\n\tEnter another number: "))
    print("\n\tVALUES BEFORE SWAPPING")
    print("\tA------------>{}".format(num1))
    print("\tB------------>{}".format(num2))
    return num1, num2


# Function to perfrom swapping of two numbers
def swap_input(n1,n2):
    n1 = n1^n2
    n2 = n2^n1
    n1 = n1^n2
    disp_results(n1,n2)

# Function to display the results
def disp_results(n1,n2):
    print("\n\tVALUES AFTER SWAPPING")
    print("\tA------------>{}".format(n1))
    print("\tB------------>{}".format(n2))
    


# Main program
val = usr_input()
swap_input(val[0],val[1])