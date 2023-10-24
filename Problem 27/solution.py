# Function to take input from the user
def usr_input():
    while True:
        num = float(input("\n\tEnter a number to check if it is divisible by both 5 AND 6: "))
        if num>0:
            break
        else:
            print("\n\tInvalid Input")
    return num

# Function to check if the input is divisible by both 5 AND 6
def check_divisibility(num):
    if num %5 == 0 and num %6 == 0:
        print("\n\t{} is divisible by both 5 AND 6".format(num))
    else:
        print("\n\t{} is not divisible by both 5 AND 6".format(num))

# Main program
num = usr_input()
check_divisibility(num)


while True:
    while True:
        condn = input("\n\tDo you want to check another number? (y/n): ")
        condn = condn.lower()
        if condn == "y" or condn == "n":
            break
    if condn == 'y':
        num = usr_input()
        check_divisibility(num)
    else:
        print("\n\tThank you!")
        break