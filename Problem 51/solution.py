# function to accept user input
def user_input():
   usr_val = int(input("\n\tEnter a number: "))
   return usr_val 

# Function to perform the conversion and display the result
def convertop(val):
    
        print("\n\t Converting {} to binary we get: {}".format(val,bin(val)))
    
    
# main program
val = user_input()
convertop(val)