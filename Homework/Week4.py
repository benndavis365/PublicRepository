def main():
  #Display intro to user
  intro()

  try:
    #Get the number of miles
    miles_needed = int(input('Enter the number of miles you drove: '))

    #Convert miles to kilometers
    miles_to_kilometers(miles_needed)

  except:
    print("That was not a valid input. Please try again")
    print()
    main()


#This function displays an intro screen to the user
def intro():
  print("This program converts miles to kilometers.")
  print("For reference the formula is: 1 mile = 1.609344 kilometers")
  print()


# The miles_to_kilometers function accepts a number of
# miles and displays the equivalent number of kilometers
def miles_to_kilometers(miles):
  kilometers = miles * 1.609344
  print('That converts to', kilometers, "kilometers")


# Calling the main function
main()
