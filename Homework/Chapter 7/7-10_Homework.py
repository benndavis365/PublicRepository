responses = {}

# Set a flag to indicate polling is active
polling_active = True

while polling_active:
  # Prompt for the users name and response
  name = input('\nWhat is your name? ')
  response = input("\nWhat is your dream vacation spot? ")

  # Store the response in the dictionary
  responses[name] = response

  # Find out if anyone else is going to take the poll
  repeat = input(
      "\nWould you like to let another person take the poll? (yes/no) ")
  if repeat == 'no':
    polling_active = False

# Polling is complete. Showing results

print("\n ---Poll Results--- ")
for name, response in responses.items():
  print(f"{name.title()} would like to go to {response.title()}.")
