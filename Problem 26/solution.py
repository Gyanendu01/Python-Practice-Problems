# Function to accept a number from the user
def usr_input():
    num = float(input("\tEnter a number: "))
    return num

# Function to check whether the number is +ve -ve or 0
def check_num(num):
    if num > 0:
        print("\n\tNumber is positive")
    elif num < 0:
        print("\n\tNumber is negative")
    elif num == 0:
        print("\n\tNumber is zero")

# Main program
num = usr_input()
check_num(num)

while True:
    while True:
        condn = input("\n\tDo you want to check another number? (y/n): ")
        condn = condn.lower()
        if condn == "y" or condn == "n":
            break
    if condn == 'y':
        num = usr_input()
        check_num(num)
    else:
        print("\n\tThank you!")
        break