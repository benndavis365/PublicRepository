class Restaurant:
  def __init__(self,restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type

  
  
  def describe_restaurant(self):
    print(f"\nThe name of the restaurant is {self.restaurant_name}")
    print(f"They serve {self.cuisine_type}")

  def open_restaurant(self):
    print(f"{self.restaurant_name} is open!")



restaurant = Restaurant("Bubba Gumps", "Shrimpies")
restaurant_2 = Restaurant("Chubbies", "Burgers")
restaurant_3 = Restaurant("Abuelas", "Tex-Mex")

restaurant.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
#restaurant.open_restaurant()