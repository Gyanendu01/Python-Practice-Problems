# largest of three numbers using anonymous function
max_num = lambda x,y,z: x if x>y and x>z else y if y>x and y>z else z

# Main program
max_value = max_num(int(input("\tEnter the First value: ")),int(input("\n\tEnter the Second value: ")),int(input("\n\tEnter the Third value: ")))
print("\n\tMax Value: {}".format(max_value))