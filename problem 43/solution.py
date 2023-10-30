# Function to accept user input
def usr_input():
    while True:
        operation = input("\n\tIF YOU WANT TO CONVERT HOURS TO SECONDS ENTER(hs)\n\tIF YOU WANT TO CONVERT SECONDS TO HOURS ENTER(sh): ")
        operation = operation.lower()
        if operation in ["hs", "sh"]:
            break
        else:
            print("\n\tEnter Correct input")
    if operation == "hs":
        val = float(input("\n\tEnter The time in hours to convert it to seconds: "))
    
    if operation == "sh":
        val = float(input("\n\tEnter The time in seconds to convert it to hours: "))
    return operation,val

# Function to perform operation and dsiplay the result
def disp_results(op,val):
    if op == "hs":
        print("\n\tCONVERTING HOURS({}) TO SECONDS".format(val))
        print("\n\t{}".format(val*3600))
    
    if op == "sh":
        print("\n\tCONVERTING SECONDS({}) TO HOURS".format(val))
        print("\n\t{}".format(val/3600))

# Main Program
res = usr_input()
disp_results(res[0],res[1])
while True:
    while True:
        condn = input("\n\tDo you want to check more subjects? (y/n): ")
        condn = condn.lower()
        if condn in ["y","n"]:
            break
    if condn == "y":
        res = usr_input()
        disp_results(res[0],res[1])
    else:
        print("\n\tTHANK YOU")
        break
