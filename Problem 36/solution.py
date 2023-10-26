#   Function to accpet user input
def usr_input():
    while True:
        val = int(input("\tEnter a number greater than 0 from keyboard: "))
        if val > 0:
            break
        else:
            print("\n\tEnter a valid input")
    return val

# Function to perform the desired action and display the results
def disp_res(val):
    print("\n\tNumber\t\tSquare\t\tCube\t\tSum")
    sum = 0
    for i in range(val,-3,-4):
        if i<=1:
            break
        sum = sum+i
        print("\t{}\t\t{}\t\t{}\t\t{}".format(i,i**2,i**3,sum))

# Main program
value = usr_input()
disp_res(value)

while True:
    while True:
        condn = input("\n\tDo you want to check another number? (y/n): ")
        condn = condn.lower()
        if condn == "y" or condn == "n":
            break
    if condn == 'y':
        value = usr_input()
        disp_res(value)
    else:
        print("\n\tThank you!")
        break