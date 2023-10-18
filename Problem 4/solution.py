# Taking Input from the User 
def readval():
    name = input("\tEnter Your Name: ")
    while True:
        age = int(input("\tEnter your Age: "))
        if age > 0:
            break
        else:
            print("\tInvalid Input")
    return name,age

# Display Function
def dispval(name,age):
    print("\n\tHi {}! Your age is {}".format(name, age))

#Main Program
val = readval()
dispval(val[0],val[1])