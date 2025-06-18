# Class: MovieReview
# Takes movie_name and rating.
# Method review() should return:
# "Excellent" if rating ≥ 8
# "Average" if 5 ≤ rating < 8
# "Poor" otherwise

class MovieReview:
    def __init__(self,movieName,rating):
        self.movieName=movieName
        self.rating=rating
    def review(self):
        if self.rating>=8:
            print("Excellent")
        elif 5 <= self.rating <8:
            print("Average")
        else:
            print("Poor")

rating=MovieReview('abc movie',10)
rating.review()