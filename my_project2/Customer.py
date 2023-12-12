from Reviews import Review

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    @property
    def given_name(self):
        return self._given_name

    @given_name.setter
    def given_name(self, new_name):
        self._given_name = new_name

    @property
    def family_name(self):
        return self._family_name

    @family_name.setter
    def family_name(self, new_name):
        self._family_name = new_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    def restaurants(self):
        return list(set([review.restaurant() for review in self.reviews]))

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.add_review(review)

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def all(cls):
        return cls.all_customers

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        customers = []
        for customer in cls.all_customers:
            if customer.given_name == name:
                customers.append(customer)
        return customers