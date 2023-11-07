# Function to add user input
def user_input():
    user_input = input("\n\tWrite some lines on any topic: ")
    return user_input

# Function to perform the desired operation and display the result

def perform_operation(usr_data):
    usr_data = usr_data.split(" ")
    no_ofword = len(usr_data)
    no_ofletter = 0
    for i in usr_data:
            no_ofletter = no_ofletter + len(i)

    print("\n\tNumber of words in the paragraph provided by the user: {}".format(no_ofword))
    print("\n\tNumber of letters in the paragraph provided by the user: {}".format(no_ofletter))

# main program

data = user_input()
perform_operation(data)