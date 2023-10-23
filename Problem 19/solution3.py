# Anonymous Function to find the smallest value
small_val = lambda x: min(lst)


# Creation of list
print("\tEnter the elements in the list separated by space")
lst = [int(x) for x in input().split()]


# Display results
print("\n\tThe provided list: {}".format(lst))
print("\tThe smallest element in the list: {}".format(small_val(lst)))

