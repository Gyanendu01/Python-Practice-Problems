from datetime import date

# Function to get user input
def usr_input():
    while True:
        usr_input = input("\n\t Do you want to see current date (y/n)?: ")
        usr_input = usr_input.lower()
        if usr_input in ["y","n"]:
            break
        else:
            print("\n\tEnter a correct input...")
        
    return usr_input

# Function to display date
def display_date(usr_input):
    if usr_input == "y":
        print("\n\tCuurent date is: {}".format(date.today()))

    else:
        print("\n\tThank you")

# Main function
val = usr_input()
display_date(val)