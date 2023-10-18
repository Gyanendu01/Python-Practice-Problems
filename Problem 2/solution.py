import math

# Taking input from the User 
def readval():
    while True:
        rad = float(input("\tEnter The Radius of the Circle: "))
        if rad > 0:
            break
        else:
            print("\tInvalid Input")
    return rad


# Fuction to calculate area of the circle and display the result
def ar_circle(rad):
    ar =round(math.pi*(rad*rad),3)
    print("\n\tArea of the Circle is: {}".format(ar))


#Main Program(Function Call)
val = readval()
ar_circle(val)