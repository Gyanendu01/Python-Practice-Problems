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