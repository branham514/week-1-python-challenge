class Restaurant:
    all_restaurants = []

    def __init__(self, name=""):
        self._name = name
        self.reviews = []  
        Restaurant.all_restaurants.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def add_review(self, review):
        self.reviews.append(review)

    def customers(self):
        return set(review.customer() for review in self.reviews)

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum(review.rating() for review in self.reviews)
        return total_ratings / len(self.reviews)