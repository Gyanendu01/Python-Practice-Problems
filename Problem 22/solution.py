#Fuction to Perform Addition on Two Input Values
def addop():
    num1 = float(input("\tEnter The First Number For Addition: "))
    num2 = float(input("\tEnter The Second Number For Addition: "))
    print("\tThe sum({},{}) = {}".format(num1, num2, num1+num2))

#Fuction to Perform Subtraction on Two Input Values
def subop():
    num1 = float(input("\n\tEnter The First Number For Subtraction: "))
    num2 = float(input("\tEnter The Second Number For Subtraction: "))
    print("\tThe subtraction({},{}) = {}".format(num1, num2, num1-num2))

#Fuction to Perform Multiplication on Two Input Values
def mulop():
    num1 = float(input("\n\tEnter The First Number For Multiplication: "))
    num2 = float(input("\tEnter The Second Number For Multiplication: "))
    print("\tMultiplication({},{}) = {}".format(num1, num2, num1*num2))

#Fuction to Perform Division on Two Input Values    
def divop():
    num1 = float(input("\n\tEnter The First Number For Division: "))
    num2 = float(input("\tEnter The Second Number For Division: "))
    print("\tThe Division({},{}) = {}".format(num1, num2, num1/num2))

#Fuction to Perform Floor Division on Two Input Values 
def floor_divop():
    num1 = float(input("\n\tEnter The First Number For Floor Division: "))
    num2 = float(input("\tEnter The Second Number For Floor Division: "))
    print("\tThe Floor Division({},{}) = {}".format(num1, num2, num1//num2))

#Fuction to Perform Modulo Division on Two Input Values 
def modulo_divop():
    num1 = float(input("\n\tEnter The First Number For Modulo Division: "))
    num2 = float(input("\tEnter The Second Number For Modulo Division: "))
    print("\tThe Modulo Division({},{}) = {}".format(num1, num2, num1%num2))


#Fuction to Perform Exponentiation on Two Input Values 
def expoop():
    num1 = float(input("\n\tEnter The Base Value For Exponentiation: "))
    num2 = float(input("\tEnter The Exponent Value For Exponentiation: "))
    print("\tThe Exponentiation of {} raised to the power {} = {}".format(num1, num2, num1**num2))


#Main Program
print("\tList of avilable operators: ")
print("\t + \n\t - \n\t * \n\t / \n\t // \n\t % \n\t **")
operator = input("\n\tEnter the operator: ")
if operator in ['+','-','*','/','//','%','**']:
   if operator == '+': 
        addop()
   elif operator == '-':
        subop()
   elif operator == '*':
        mulop
   elif operator == '/':
        divop()
   elif operator == '//':
        floor_divop()        
   elif operator == '%':
        modulo_divop()        
   elif operator == '**':
        expoop()        
else:
    print("\n\tProvided operator is not supported")




