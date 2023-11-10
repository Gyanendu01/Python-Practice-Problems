# function to input elements in a list
def user_input():
    print("\n\tEnter the elements in the list separated by spaces......")
    usr_data = [int(x) for x in input().split()]
    return usr_data

# function to perform the operation 
def perform_operation(usr_data):
    max_value = max(usr_data)
    return max_value

# function to display the result
def display_result(usr_data,max_val):
    print("\n\tProvided User data.........")
    print("\t{}".format(usr_data))
    print("\n\tMax Value in the provided data is {}".format(max_val))

# main program
usr_val = user_input()
max_val = perform_operation(usr_val)
display_result(usr_val,max_val)
