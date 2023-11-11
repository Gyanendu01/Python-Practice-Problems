# function to get data from the user
def get_data():
    side = float(input("\n\tEnter the length of the side of square: "))
    return side

# function to find area of square
def get_area(sd):
    print("\n\tArea of square is {}".format(sd*sd))

# function to find perimeter of square
def get_perimeter(sd):
    print("\n\tPerimeter of square is {}".format(sd*4))

# main program
val = get_data() 
get_area(val)
get_perimeter(val)


