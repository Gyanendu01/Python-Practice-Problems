# function to accept user input
def accept_author_name():
    athr_name = []
    for i in range(1,6):
        ele = input("\n\tEnter author name {}: ".format(i))
        athr_name.append(ele)
    return athr_name

# function to accpet book name associated with the author
def accept_book_name(athr_name):
    book_name = []
    for i in athr_name:
        ele = input("\n\tEnter a book name by {}: ".format(i))
        book_name.append(ele)
    return book_name

# function to display the desired result
def display_result(book_name,author_name):
    print("\n\ta book by {} is {}".format(author_name[-1],book_name[-1]))


# main program
author_name = accept_author_name()
print("\n\t","="*44)
book_name = accept_book_name(author_name)
display_result(book_name,author_name)