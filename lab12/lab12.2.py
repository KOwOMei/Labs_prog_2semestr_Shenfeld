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
    def __init__(self, restaurant_name, cuisine_type, flavors, location, work_time):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.work_time = work_time
    
    def show_flavors(self):
        print("List of ice cream flavors:")
        for flavor in self.flavors:
            print("- " + flavor)
    
    def add_flavor(self, new_flavor):
        self.flavors.append(new_flavor)
        print("Ice cream flavor " + new_flavor + " has been added to the menu.")
    
    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print("Ice cream flavor " + flavor + " has been removed from the menu.")
        else:
            print("This ice cream flavor is not available in the menu.")
    
    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print("Ice cream flavor " + flavor + " is available.")
        else:
            print("This ice cream flavor is not available.")

class IceCreamBar(IceCreamStand):
    def __init__(self, restaurant_name, cuisine_type, flavors, location, work_time, stick_icecream_flavors):
        super().__init__(restaurant_name, cuisine_type, flavors, location, work_time)
        self.stick_icecream_flavors = stick_icecream_flavors
    
    def show_stick_icecream_flavors(self):
        print("List of ice cream on a stick flavors:")
        for flavor in self.stick_icecream_flavors:
            print("- " + flavor)

myIceCreamStand = IceCreamStand("Frosty", "Ice Cream Cafe", ["vanilla", "strawberry", "chocolate"], "Lenin avenue, 10", "10:00-22:00")
myIceCreamStand.show_flavors()
myIceCreamStand.add_flavor("caramel")
myIceCreamStand.remove_flavor("chocolate")
myIceCreamStand.check_flavor("vanilla")
myIceCreamStand.check_flavor("chocolate")

myStickIceCreamBar = IceCreamBar("Lollipop", "Ice Cream Cafe", ["vanilla", "strawberry", "chocolate"], "Pushkin street, 5", "09:00-23:00", ["watermelon", "apple", "orange"])
myStickIceCreamBar.show_stick_icecream_flavors()
