from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    reviews = relationship("Review", back_populates="customer")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        if not self.reviews:
            return None
        return max(self.reviews, key=lambda review: review.star_rating).restaurant

    def add_review(self, restaurant, rating, comments):
        new_review = Review(star_rating=rating, comments=comments, restaurant=restaurant)
        self.reviews.append(new_review)
        return new_review

    def delete_reviews(self, restaurant):
        self.reviews = [review for review in self.reviews if review.restaurant != restaurant]

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews = relationship("Review", back_populates="restaurant")

    @classmethod
    def fanciest(cls, session):
        return max(session.query(cls).all(), key=lambda restaurant: restaurant.price)

    def all_reviews(self):
        return [review.full_review() for review in self.reviews]

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    comments = Column(String)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))

    customer = relationship("Customer", back_populates="reviews")
    restaurant = relationship("Restaurant", back_populates="reviews")

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars. Comments: {self.comments}"

if __name__ == "__main__":
    engine = create_engine('sqlite:///reviews.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    def get_user_input():
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        restaurant_name = input("Enter the restaurant name: ")
        rating = int(input("Enter your rating (1-5): "))
        comments = input("Enter your comments: ")

        return first_name, last_name, restaurant_name, rating, comments

    try:
        first_name, last_name, restaurant_name, rating, comments = get_user_input()

        # Check if the customer already exists, if not, create a new customer
        customer = session.query(Customer).filter_by(first_name=first_name, last_name=last_name).first()
        if not customer:
            customer = Customer(first_name=first_name, last_name=last_name)
            session.add(customer)

        # Check if the restaurant already exists, if not, create a new restaurant
        restaurant = session.query(Restaurant).filter_by(name=restaurant_name).first()
        if not restaurant:
            restaurant = Restaurant(name=restaurant_name, price=3)  # You may want to prompt the user for the price
            session.add(restaurant)

        # Add the review
        new_review = customer.add_review(restaurant, rating, comments)
        session.commit()

        print("Review added successfully!")
        print(new_review.full_review())

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the session
        session.close()