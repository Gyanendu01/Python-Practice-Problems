# Function to input user name and marks
def usr_data():
    name = input("\n\tEnter your username: ")
    usr_marks = []
    print("\n\tEnter the name of subjects separated by space: ")
    sub_names = [str(x) for x in input().split()]
    for i in sub_names:
        ele = int(input("\n\tEnter the marks in {}: ".format(i)))
        usr_marks.append(ele)
    return name, usr_marks, sub_names

# Function to calculate average
def usr_average(usr_marks):
    tot_marks = 0
    for i in usr_marks:
        tot_marks = tot_marks + i
    avg_marks = tot_marks/len(usr_marks)
    return avg_marks

# Function to display the results
def usr_results(name, usr_marks, sub_names,avg_marks):
    print("\n\tHello {} ".format(name))
    print("\n\tALL SUBJECT MARKS")
    z = zip(sub_names, usr_marks)
    print("\n\tSUBJECT NAME\t\tSUBJECT MARKS")
    for i,j in z:
        print("\n\t{}\t\t\t{}".format(i, j))
    print("\n\tAVERAGE MARKS: {}".format(avg_marks))

# Main program
val = usr_data()
avg = usr_average(val[1])
usr_results(val[0],val[1],val[2],avg)