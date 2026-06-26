# Create a class Book with the following attributes: title,author,list of reviews
# And add methods to: add a new review,count reviews,display all reviews

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.ListOfReviews=[]
        
    def add_review(self,NewReview):
        self.ListOfReviews.append(NewReview)
        print(f"Review added for '{self.title}'!")

    def count_review(self):
        print(f"the number of reviews in '{self.title}' are: {len(self.ListOfReviews)}")

    def display_reviews(self):
        print(f"all the reviews of {self.title} are-")
        for i in self.ListOfReviews:
            print(i)

b1=Book("Twisted Game","ana huang")
b1.add_review("loved it!")
b1.add_review("amazing story!")
b2=Book("Atomic Habbit","James Clear")
b2.add_review("life-changing")
b2.count_review()
b1.display_reviews()

