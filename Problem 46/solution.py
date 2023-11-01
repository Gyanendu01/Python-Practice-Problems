# Function to take a sentence as input from user
def user_input():
    usr_sentence = input("\n\tEnter a sentence separated by spaces: ")
    return usr_sentence

# Function to perform the desired operation
def perform_operation(sentc):
    lst = sentc.split(" ")
    lst.reverse()
    for i in lst:
        print("\n\t{}".format(i),end=" ")
        
    print(".")

    
# Main program
val = user_input()
perform_operation(val)