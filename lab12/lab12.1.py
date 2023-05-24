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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def show_flavors(self):
        print("List of ice cream flavors:")
        for flavor in self.flavors:
            print("- " + flavor)

myIceCreamStand = IceCreamStand("Frosty", "Ice Cream Cafe", ["vanilla", "strawberry", "chocolate"])
myIceCreamStand.show_flavors()
