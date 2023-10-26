# Function to get username
def get_username():
    while True:
        usr_name = input("\n\tEnter a username(Alphanumeric and Min 8 characters): ")
        if len(usr_name) > 8:
            if usr_name.isalnum():
                break
            else:
                print("\tInvalid username.....Please enter a valid username")
        else:
            print("\tInvalid username.....Please enter a valid username")
    return usr_name

# Function to display the username
def display_username(name):
    print("\n\tUser name entered is: {}".format(name))

# main Program
value = get_username()
display_username(value)