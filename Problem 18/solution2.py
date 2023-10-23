# list creation and finding the lasrgest value
print("\tEnter the elements in the list separated by space")
lst = [int(x) for x in input().split()]

# Using the MAX() function to find the largest element
big_val = max(lst)

print("\n\tThe provided list: {}".format(lst))
print("\tThe largest element in the list: {}".format(big_val))