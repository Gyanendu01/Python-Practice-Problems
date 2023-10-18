# Taking Input From the user
def readval():
    while True:
        val = int(input("\tEnter The End value Till Which You would like to find square and cube of: "))
        if val >= 0:
            break
        else:
            print("\tInvalid Input")
    return val

# Logic of the program along with the output
def operation(val):
    print("\n\tNumber\t\tSquare\t\tCube")
    for i in range(1,val+1):
        print("\t{}\t\t{}\t\t{}".format(i,i**2,i**3))

# Main Program ( funcation call )
val = readval()
operation(val)