#To create functions and push book IDs into stack, check for empty stack and pop the topmost stack object. Also check for stack underflow!
books={"B101":245,"B102":380,"B103":290,"B104":425,"B105":315,"B106":275}
long_books=[]
def PushBooks():
    for bookid in books:
        if books[bookid]>=300:
            long_books.append(bookid)
def IsEmpty():
    if long_books:
        return False
    else:
        return True
def PopBooks():
    if not IsEmpty():
        return long_books.pop()
    else:
        print("No long book!")
PushBooks()
print(IsEmpty())
print(PopBooks())