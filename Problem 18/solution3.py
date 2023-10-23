# Anonymous Function to find the largest value
big_val = lambda x: max(lst)


# Creation of list
print("\tEnter the elements in the list separated by space")
lst = [int(x) for x in input().split()]


# Display results
print("\n\tThe provided list: {}".format(lst))
print("\tThe largest element in the list: {}".format(big_val(lst)))

