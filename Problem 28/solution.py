# Function accept mark from user
def accept_mark():
    while True:
        usr_mark = float(input("\n\tEnter your mark: "))
        if usr_mark >= 0:
            break
        else:
            print("\n\tInvalid Input")
    return usr_mark

# Function to check Grade
def grade(mark):
    if mark >= 95:
        print("\n\tA+ GRADE")
    elif mark >= 80 and mark < 95:
        print("\n\tA GRADE")
    elif mark >= 70 and mark < 80:
        print("\n\tB GRADE")
    elif mark >= 60 and mark < 70:
        print("\n\tC GRADE")
    else:
        print("\n\tFAIL")

# Main program
num = accept_mark()
grade(num)


while True:
    while True:
        condn = input("\n\tDo you want to check another number? (y/n): ")
        condn = condn.lower()
        if condn == "y" or condn == "n":
            break
    if condn == 'y':
        num = accept_mark()
        grade(num)
    else:
        print("\n\tThank you!")
        break