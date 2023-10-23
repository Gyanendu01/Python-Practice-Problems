# Function to take input from the user
def readval():
    while True:
        val = input("\tEnter a value: ")
        if len(val) == 1:
            break
        else:
            print("Invalid input! Please enter a single character")

    return val

# Function to check if the provided input is vowel or consonant or a number and display the result
def checkval(val):
    if val.isalpha():
        val = val.lower()
        if val in ['a','e','i','o','u']:
            print("\n\t{} is a vowel".format(val))
        else:
            print("\n\t{} is a consonant".format(val))

    elif val.isdigit():
        print("\n\t{} is a digit".format(val))
    else:
        print("\n\t{} is a special symbol".format(val))


# Main program
val = readval()
checkval(val)