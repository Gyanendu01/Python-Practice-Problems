# Function to accept some values from user
def usr_input():
    print("\n\tEnter some elements from the keyboard separated by spaces")
    ele_lst = [int(x) for x in input().split()]
    return ele_lst

# Function to seacrh for the required element and display the index
def check_ele(lst):
    ele = int(input("\n\tEnter the element you want to search for: "))
    found = False
    for i in lst:
        if i==ele:
            found = True
            break
        else:
            found = False
    if found:
            print("\n\tThe specified element({}) is present in the list of elements".format(i))
            print("\tThe index of the specified element is {}".format(lst.index(i)))
    else:
            print("\n\tThe specified element({}) is not present in the list of elements".format(ele))
# Main program
ele = usr_input()
check_ele(ele)