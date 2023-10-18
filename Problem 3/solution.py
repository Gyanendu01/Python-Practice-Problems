# Taking Input from the User 
def readval():
    length = float(input("\tEnter the length of the rectangle: "))
    width = float(input("\tEnter the width of the rectangle: "))
    return width, length


# Area Calculation Function 
def rect_area(len,wid):
    area = len*wid
    return area

# Display Of Area Calculation Function
def disp_area(val1,val2,ar):
    print("\n\tThe Area Of the rectangle with length({}) and width({}) is {}".format(val1,val2,ar))


#Main Program
val = readval()
res = rect_area(val[0],val[1])
disp_area(val[0],val[1],res)