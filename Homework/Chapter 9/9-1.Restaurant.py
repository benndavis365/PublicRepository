class Restaurant:
  def __init__(self,restaurant_name, cuisine_type):
    self.restaurant_name = name
    self.cuisine_type = type

  
  
  def describe_restaurant(self):
    print(f"The name of the restaurant is {self.restaurant_name}")
    print(f"\tThey serve {self.cuisine_type")

  def open_restaurant(self):
    print(f"{self.restaurant_name} is open!")



restaurant = Restaurant("Bubba Gumps", "Shrimpies")