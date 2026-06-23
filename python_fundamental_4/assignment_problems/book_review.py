# Create a class Book with the following attributes: title,author,list of reviews
# And add methods to: add a new review,count reviews,display all reviews

#class Book:
    #def __init__(self,title,author,listOfReviews):
        #self.title=title
        #self.author=author
        #self.listOfReviews=listOfReviews

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        """Adds a new review to the book."""
        self.reviews.append(review)

    def count_reviews(self):
        """Returns the total number of reviews."""
        return len(self.reviews)

    def display_reviews(self):
        """Prints all reviews for the book."""
        if not self.reviews:
            print(f"No reviews for '{self.title}' yet.")
            return
        
        print(f"Reviews for '{self.title}' by {self.author}:")
        for index, review in enumerate(self.reviews, start=1):
            print(f"{index}. {review}")
