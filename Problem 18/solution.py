# Function For the dynamic creation of the list object
def create_list():
    print("\tEnter the elements in the list object separated by space")
    lst = [int(x) for x in input().split()]
    return lst

# Function to find the largest element in the list
def big_val(lst):
    big_val = lst[0]
    for i in lst:
        if i > big_val:
            big_val = i
    return big_val

# Function to display the result
def display_result(lst,big_val):
    print("\n\tThe provided list: {}".format(lst))
    print("\tThe largest element in the list: {}".format(big_val))

# Main program
val = create_list()
big_val = big_val(val)
display_result(val,big_val)