# Function For the dynamic creation of the list object
def create_list():
    print("\tEnter the elements in the list object separated by space")
    lst = [int(x) for x in input().split()]
    return lst

# Function to find the smallest element in the list
def small_val(lst):
    small_val = lst[0]
    for i in lst:
        if i < small_val:
            small_val = i
    return small_val

# Function to display the result
def display_result(lst,small_val):
    print("\n\tThe provided list: {}".format(lst))
    print("\tThe smallest element in the list: {}".format(small_val))

# Main program
val = create_list()
small_val = small_val(val)
display_result(val,small_val)