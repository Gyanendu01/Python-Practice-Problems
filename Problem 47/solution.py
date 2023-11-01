# Function to get age from the user
def usr_age():
    usr_age = int(input("\n\tEnter your age: "))
    return usr_age

# Function to perfrom the desired operation and display the result
def disp_usr(age):
    print("\n\tYour age in \n\thours: {} \n\tminutes: {} \n\tseconds: {} ".format((age*24*365),(age*24*60*365),(age*24*60*60*365)))

# Main program
age = usr_age()
disp_usr(age)