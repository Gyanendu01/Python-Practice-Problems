# Function to accept 6 values from the keyboard
def usr_input():
    print("\n\tEnter 6 Numbers from the keyboard separated by space: ")
    num = list()
    for i in range(1,7):
        ele = int(input("\tEnter element {}: ".format(i)))
        num.append(ele)
    return num

# Function to find square of first three and cube of last three
def disp_val(num):
    print("\n\tSQUARE OF FIRST THREE NUMBERS")
    print("\t","="*28)
    
    for i in range(0,3):
        print("\t",num[i]**2,end=" ")
    
    print("\n\tCUBE OF LAST THREE NUMBERS")
    print("\t","="*26)

    for i in range(3,6):
        print("\t",num[i]**3,end=" ")
    
# Main program
val = usr_input()
disp_val(val)