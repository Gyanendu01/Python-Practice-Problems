first_name = input("\n\tEnter your first name: ")
first_name = first_name.split(" ")
first_name = first_name[0]

last_name = input("\n\tEnter your last name: ")
last_name = last_name.split(" ")
last_name = last_name[0]

print("\n\tHello, {} {}".format(first_name.title(), last_name[0]))