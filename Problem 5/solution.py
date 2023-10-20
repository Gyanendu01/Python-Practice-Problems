# Taking Input from the User 
def readval():
    name = input("\tEnter your Name: ")
    while True:
        age = int(input("\tHi, {} Enter Your Age: ".format(name)))
        if age > 0:
            break
        else:
            print("\tInvalid Input")
    return name,age

#Check Age Of User using Fuction
def check_age(name,age):
    if age >= 18:
        print("\n\t{} You can VOTE".format(name))
    else:
        year_of_vote = 18 - age
        print("\n\tSorry {} you cannot VOTE. You can VOTE after {} years ".format(name,year_of_vote))


#Main Program
val = readval()
check_age(val[0],val[1])