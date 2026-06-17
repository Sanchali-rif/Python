# Create a class Book with the following attributes: title,author,list of reviews
# And add methods to: add a new review,count reviews,display all reviews

class Book:
    def __init__(self,title,author,listOfReviews):
        self.title=title
        self.author=author
        self.listOfReviews=listOfReviews