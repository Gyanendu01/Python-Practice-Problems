# Function to take name of the week from the user
def readval():
    usr_input = input("\tEnter the name of the week: ")
    return usr_input

# Function to check if the provided input is a holiday or not
def check_holiday(input):
    input = input.lower()
    if input in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
        if input in ["friday","sunday"]:
            print("\n\t{} IS A HOLIDAY".format(input.upper()))
        else:
            print("\n\t{} IS NOT A HOLIDAY".format(input.upper()))
    else:
        print("\n\tProvided week name is not a valid week name")
       

# Main Program
input = readval()
check_holiday(input) 