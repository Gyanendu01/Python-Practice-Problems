# Function to accept the end-term from the user
def read_endterm():
    while True:
        enterm_val = int(input("\tEnter the end term value to find all the even numbers between 1 and end-term: "))
        if enterm_val > 0:
            break
        else:
            print("\n\tEnter a positive number....")
    return enterm_val

# Function to display the even numbers between 1 and end-term
def disp_val(val):
    print("\n\tEVEN NUMBERS ARE")
    for i in range(2,val+2,2):
        print("\n\t{}".format(i),end=" ")

# Main Program
val = read_endterm()
disp_val(val)

while True:
    while True:
        condn = input("\n\tDo you want to check another number? (y/n): ")
        condn = condn.lower()
        if condn == "y" or condn == "n":
            break
    if condn == 'y':
        val = read_endterm()
        disp_val(val)

    else:
        print("\n\tThank you!")
        break