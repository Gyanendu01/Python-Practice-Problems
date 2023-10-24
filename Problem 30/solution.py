# Program to accept names from the user
def usr_input():
    print("\n\tEnter names of some students from the keyboard")
    
   
    lst_names = [str(x) for x in input().split()]
    
    return lst_names

# Program to delete the first and last names and display the resut
def updated_names(lst):
    print("\n\tOriginal Names")
    print("\t","="*13)
    for i in lst:
        print(i,end=" ")
    
    print("\n")
    print("\n\tUpdated Names")
    print("\t","="*13)
    
    updated_names = lst
    updated_names.pop(0)
    updated_names.pop(-1)
    for j in updated_names:
        print(j,end=" ")

# Main Program
names = usr_input()
updated_names(names)