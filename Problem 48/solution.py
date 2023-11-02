import time as t
# Function to accept input from thye user
def usr_input():
    usr_input = int((input("\n\tEnter a number: ")))
    return usr_input

# Function to calculate the factorial of the number
def cal_factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact

# Function to display the result
def display_factorial(num,fact):
    print("\n\tFcatorial of {} is : {}".format(num,fact))

# main program
val = usr_input()
fact = cal_factorial(val)
print("\n\tPerforming Calculations......")
t.sleep(5)
display_factorial(val,fact)