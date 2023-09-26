def main():
#Display intro to user
    intro()

    try:
#Get the number of gallons
      gallons_needed = int(input('Enter the number of gallons: '))

#Convert gallons to liters
      gallons_to_liters(gallons_needed)

    except:
      print("That was not a valid input. Please try again")
      print()
      main()


#This function displays an intro screen to the user
def intro():
  print("This program converts gallons to liters.")
  print("For reference the formula is: 1 gallon = 3.785412 liters")
  print()

# The gallons_to_liters function accepts a number of 
# gallons and displays the equivalent number of liters
def gallons_to_liters(gallons):
  liters = gallons * 3.785412
  print('That converts to', liters, "liters")

# Calling the main function
main()