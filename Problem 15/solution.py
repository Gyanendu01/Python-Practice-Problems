# Function for creating a tuple object
def create_tuple():
    t1 = (1,3,22.4,5,6,"python",1,2,True)
    return t1

# Function To display tuple object and also clear all elements from the tuple object
def disp_tuple(t1):
    print("\t{}".format(t1))
    t1 = ()
    print("\t{}".format(t1))

# Main Program
val = create_tuple()
disp_tuple(val)