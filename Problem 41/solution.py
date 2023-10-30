import time
# Function to get user input
def usr_input():
    num1 = float(input("\n\tEnter a number: "))
    num2 = float(input("\n\tEnter another number: "))
    return num1, num2

# Function to find cube of the numbers and add them
def find_cube(num1,num2):
    sum_ofcubes = num1**3 + num2**3
    return sum_ofcubes
    

# Function to display the results
def display_results(n1,n2,sum):
    print("\n\tSUM OF CUBES({} and {}) = {}".format(n1,n2,sum))

# Main program
num = usr_input()
res = find_cube(num[0],num[1])
print("\n\tPerforming Your Desired Operation..")
time.sleep(5)
display_results(num[0],num[1],res)