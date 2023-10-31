# Function to take user input
def user_input():
    len = float(input("\n\tEnter the length of the traingle: "))
    bred = float(input("\tEnter the breadth of the traingle: "))
    return len,bred

# Function to calculate the area of the traingle
def area_of_traingle(len,bred):
    ar = 0.5*len*bred
    print("\n\tArea of the traingle is {}".format(ar))
    num = float(input("\n\tEnter a number: "))
    print("\n\tAdding the number to the result we get {}".format(ar+num))

# main program
val = user_input()
area_of_traingle(val[0],val[1])
while True:
    while True:
        condn = input("\n\tDo you want to check more subjects? (y/n): ")
        condn = condn.lower()
        if condn == "y" or condn == "n":
            break
    if condn == "y":
        val = user_input()
        area_of_traingle(val[0],val[1])
    else:
        print("\n\tTHANK YOU")
        break