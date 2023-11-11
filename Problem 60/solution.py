# function to get user_marks

def get_user_marks():
   print("\n\tSee the criteria") 
   print("\n\n\tMarks Equal To 1100\t\t  Free Education\n\tMarks > 1000 and Marks < 1100\t\t  80% Monthly Fees Deduction\n\tMarks > 900 and Marks < 1000\t\t  60% Monthly Fees Deduction\n\tMarks > 800 and Marks < 900\t\t  40% Monthly Fees Deduction\n\tMarks > 700 and Marks < 800\t\t  30% Monthly Fees Deduction\n\tMarks > 600 and Marks < 700\t\t  There Is No Scholarship")

   print("\n\n\tMONTHLY FEES------------> $1100")
   
   mark = int(input("\n\tEnter your marks: "))
   return mark

# function to provide scholarship
def scholarship_reslt(mark):
   if mark == 1100:
      print("\n\tCongratulations! you have secured a Free Education scholarship")
   elif mark > 1000 and mark < 1100: 
        print("\n\tCongratulations! you have secured a scholarship")
        print("\tNow you have to pay ${} instead of ${}".format(round(mark*0.8,3),mark))
   elif mark < 1000 and mark > 900: 
        print("\n\tCongratulations! you have secured a scholarship")
        print("\tNow you have to pay ${} instead of ${}".format(round(mark*0.6,3),mark))
   elif mark > 800 and mark < 900: 
        print("\n\tCongratulations! you have secured a scholarship")
        print("\tNow you have to pay ${} instead of ${}".format(round(mark*0.4,3),mark))
   elif mark > 700 and mark < 800: 
        print("\n\tCongratulations! you have secured a scholarship")
        print("\tNow you have to pay ${} instead of ${}".format(round(mark*0.3,3),mark))
   else:
       print("\n\tSorry to say, You won't be getting any scholarship")

# main program
mark = get_user_marks()
scholarship_reslt(mark)