class Reviews:
    all_reviews=[]
    
    def __init__(self,customer,restaurant,rating:int):
        self.rating=rating
        self.customer=customer
        self.restaurant=restaurant
        Reviews.all_reviews.append(self)


    def Review_rating(self):
        return self.rating
    
    def Review_customer(self):
        return self._customer
    
    def Review_restaurant(self):
        return self._restaurant
    
    @classmethod
    def Review_all(cls):
        return cls.all_reviews