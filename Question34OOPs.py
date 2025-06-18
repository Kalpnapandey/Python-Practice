# Create a class Book with a constructor to set title and author.
# Add a method get_summary() that returns:
# "Book: <title> by <author>"
# Call this method using an object and print the result.
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def get_summary(self):
        print(f"Book:{self.title} by {self.author}")
obj=Book('It ends with us','Collen Hoover')
print(obj.get_summary())