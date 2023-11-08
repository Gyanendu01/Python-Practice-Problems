# function to accpet memory from the user

def user_input():
    while True:
        condn = input("\n\tIf you want to convert Giga-bytes to bytes enter 'GB'\n\tIf you want to convert Bytes to Giga-bytes enter 'BG':\n\t")
        condn = condn.lower()
        if condn in ['gb','bg']:
            break
    return condn

# function to