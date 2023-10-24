# Function to take marks as input from the student
def read_marks():
    usr_name = input("\tEnter your name: ")
    usr_marks = float(input("\tEnter your marks: "))
    return usr_name,usr_marks

# Function to check PASS or FAIL and display the results
def check_result(usr_name,usr_marks):
    if usr_marks >= 30:
        print("\n\tCongratulations {} You have PASSED".format(usr_name))
    else:
        print("\n\tSorry {} you have failed".format(usr_name))

# Main program
usr_data = read_marks()
check_result(usr_data[0],usr_data[1])

while True:
    while True:
        condn = input("\n\tDo you want to check another number? (y/n): ")
        condn = condn.lower()
        if condn == "y" or condn == "n":
            break
    if condn == "y":
        usr_data = read_marks()
        check_result(usr_data[0],usr_data[1])
    else:
        break