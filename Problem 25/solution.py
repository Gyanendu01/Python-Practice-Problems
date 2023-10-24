# Function to accept 5 years from the user
def input_year():
    print("\tEnter 5 years from the keyboard without spaces")
    yr_input = [int(x) for x in input().split()]
    return yr_input

# Function to determine the leap year
def leap_year(year):
    leap_yr = list()
    for i in year:
        if i % 4 == 0:
            leap_yr.append(i)
    return leap_yr

# Function to display the leap years
def disp_leap_yr(year, leap_years):
    print("\n\tProvided years:")
    print("\t", "=" * 10)
    for i in year:
        print(i, end=" ")

    print("\n\tLeap years:")
    print("\t", "=" * 10)
    for j in leap_years:
        print(j, end=" ")

# Main program
year = input_year()
res = leap_year(year)
disp_leap_yr(year, res)
