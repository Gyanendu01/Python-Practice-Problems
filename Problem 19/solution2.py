# list creation and finding the lasrgest value
print("\tEnter the elements in the list separated by space")
lst = [int(x) for x in input().split()]

# Using the MIN() function to find the largest element
small_val = min(lst)

print("\n\tThe provided list: {}".format(lst))
print("\tThe smallest element in the list: {}".format(small_val))