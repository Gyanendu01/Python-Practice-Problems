# Function to accept a sentence from the user
def usr_input():
    usr_input = input("\n\tEnter a sentence: ")
    print("\n\tUser input: {}".format(usr_input))
    usr_input = usr_input.upper()
    return usr_input

# Function to display the result 
def display_res(usr_input):
    print("\n\tUser input: {}".format(usr_input))

# Main function
value = usr_input()
display_res(value)
