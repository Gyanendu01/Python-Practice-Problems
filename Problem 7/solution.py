#Fuction to create a set Object
def read_set():
    sz1 = int(input("\tEnter The size Of First Set Object: "))
    sz2 = int(input("\tEnter The size Of Second Set object: "))

    s1 = set()
    s2 = set()
    
    print("\n")
    for i in range(1,sz1+1):
        ele = int(input("\tEnter the {} element for set1: ".format(i)))
        s1.add(ele)
    
    print("\n")
    for j in range(1,sz2+1):
        ele = int(input("\tEnter the {} element for set2: ".format(j)))
        s2.add(ele)

    return s1,s2


#Performs set operations on the input set objects
def dispop(s1,s2):
    print("\n\ts1 = {}".format(s1))
    print("\ts2 = {}".format(s2))
    print("\n\tThe Union of Two sets are: {}".format(s1.union(s2))) 
    print("\tThe intersection of two sets are: {}".format(s1.intersection(s2)))
    print("\tThe Difference of two sets are: {}".format(s1.difference(s2)))
    print("\tThe Symmetric Difference of two sets are: {}".format(s1.symmetric_difference(s2)))

#Main Program
val = read_set()
dispop(val[0],val[1])