class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
    
    def describe_restaurant(self):
        print(f"Restaurant {self.restaurant_name}. Type of resturant - {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is opened!")
        
    def set_rating(self, rating):
        self.rating = rating
        print(f"{self.restaurant_name} rating is updated to {(self.rating)} points")

# 11.1)
print("11.1)")
newRestaurant = Restaurant("Markus's table", "Handmade cuisine", 0)
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
print("\n")

# 11.2)
print("11.2)")
restaurant1 = Restaurant("Romeo's Pizza", "Italian cuisine")
restaurant2 = Restaurant("Soi Sushi", "Chinese cuisine")
restaurant3 = Restaurant("Shaverma Hall", "Georgian cuisine")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
print("\n")

# 11.3)
print("11.3)")
newRestaurantRating = Restaurant("Markus's table", "Handmade cuisine", 3)
print(newRestaurantRating.rating)
newRestaurantRating.set_rating(5)