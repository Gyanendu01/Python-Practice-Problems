# Function to Input Marks
def read_marks():
    while True:
        num_sub = int(input("\thow many subjects you want to enter: "))
        if num_sub > 0:
            break
        else:
            print("\tInvalid Input")

    print("\n")
    lst_marks = list()
    for i in range(1, num_sub+1):
        mark = int(input("\tEnter Mark {}: ".format(i)))
        lst_marks.append(mark)

    return lst_marks,num_sub

# Function to find total,average,and percentage of marks and display the results in marks memo format.
def disp_marks(lst_marks,num_sub):
    print("\n\tMARKS OBTAINED IN EACH SUBJECT")
    print("\t","="*35)

    tot_marks = 0 
    for i in lst_marks:
        print("\t{}".format(i))
        tot_marks = tot_marks + i

    print("\n\tTOTAL MARKS IN ALL {} SUBJECTS".format(num_sub))
    print("\t","="*35)
    print("\tTotal Marks = {}".format(tot_marks))
     
    print("\n\t PERCENTAGE OF MARKS IN ALL {} SUBJECTS".format(num_sub))
    print("\t","="*40)
    
    print("\tPercentage of Marks = {}".format((tot_marks/(num_sub*100))*100))
     
    print("\n\tAVERAGE OF MARKS IN ALL {} SUBJECTS".format(num_sub))
    print("\t","="*35)
    print("\tAverage Marks = {}".format(tot_marks/num_sub))
     
# Main program
val = read_marks()
disp_marks(val[0],val[1])