# Function to take a sentence as input from user
def user_input():
    usr_sentence = input("\n\tEnter a sentence separated by spaces: ")
    return usr_sentence

# Function to perform the desired operation
def perform_operation(sentc):
    lst = sentc.split(" ")
    lst.reverse()
    print("\n\tYour sentence in reversed format is: ")
    for i in lst:
        print("{}".format(i),end=" ")
        
    print(".")


# Main program
val = user_input()
perform_operation(val)