# function to accpet the user details
def get_user_details():
    d = {
        'name': input("\n\tEnter your name: "),
        'father_name': input("\n\tEnter your father's name: "),
        'age': input("\n\tEnter your age: "),
        'contact_details': input("\n\tEnter your contact details: ")
    }
    return d


# function to display the results
def display_results(d):
    print("\n\t\t\t\tUSER DETAILS")
    print("\n")
    for i,j in d.items():
        print("\t{}:\t{}".format(i,j))


# main program
val = get_user_details()
display_results(val)
    