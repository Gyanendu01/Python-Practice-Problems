# Function to accept input from the user
def readval():
    a = float(input("\tEnter a number: "))
    b = float(input("\tEnter second number: "))
    c = float(input("\tEnter third number: "))
    d = float(input("\tEnter forth number: "))
    return a,b,c,d

# Function to perfrom the operation
def equation(a,b,c,d):
    val = d+a+2*a*b/d*(4*c+10)
    return val

# Function to display the result
def dispval(val):
    print("\n\tThe solution of the equation 'd+a+2*a*b/d*(4*c+10)' is: {}".format(round(val,4)))

# Mian program
val = readval()
res = equation(val[0],val[1],val[2],val[3])
dispval(res)