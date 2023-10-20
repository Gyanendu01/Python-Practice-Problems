#Function To Take Input From The User
def readval():
    num = int(input("\tEnter A Number: "))
    return num

#function to display the Multiplication Table
def mul_table(num):
    print("\n\tMULTIPLICATION TABLE FOR {}".format(num))
    print("\t","="*27)
    for i in range(1,11):
        print("\t{} X {} = {}".format(i,num,i*num))


#Main Program
val = readval()
mul_table(val)