# Function to take input from the user
def readval():
    name = input("\tEnter your name: ")
    address = input("\tEnter your address: ")
    while True:
        contact_no = (input("\tEnter your contact number: "))
        if len(contact_no) == 10:
            break
        else:
            print("\n\tInvalid contact number")
    return name, address, contact_no

# Function to display provided information
def dispval(name,add,cont):
    print("\n\tYour name is  {}".format(name))
    print("\tYour address is  {}".format(add))
    print("\tYour contact number is  {}".format(cont))

# Function to update the user's information
def updateval(name,add,updated_contact):
    while True:
        updated_contact = (input("\n\tEnter your updated contact number: "))
        if len(updated_contact) == 10:
            break
        else:
            print("\n\tInvalid contact number")
    
    print("\n\tUPDATED USER INFO")
    print("\t","="*15)
    dispval(name,add,updated_contact)

# Main program
user_info = readval()
dispval(user_info[0],user_info[1],user_info[2])
updateval(user_info[0],user_info[1],user_info[2])