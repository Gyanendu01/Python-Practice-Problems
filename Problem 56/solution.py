# function to accpet memory from the user

def user_input():
    while True:
        condn = input("\n\tIf you want to convert Giga-bytes to bytes enter 'GB'\n\tIf you want to convert Bytes to Giga-bytes enter 'BG':\n\t")
        condn = condn.lower()
        if condn in ['gb','bg']:
            break
    return condn

# function to perform operation

def operation(condn):
    if condn == 'gb':
        value = int(input("\n\tEnter a value: "))
        print("\n\t {} Giga-bytes converted to bytes: {}".format(value, value*1000))        
    
    if condn == 'bg':
        value = int(input("\n\tEnter a value: "))
        print("\n\t {} Bytes converted to Giga-bytes: {}".format(value, value/1000))        


# main program
val = user_input()
operation(val)