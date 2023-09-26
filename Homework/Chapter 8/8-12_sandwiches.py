def make_sandwich(*toppings):
  print(f"\nMaking a sandwich with the following toppings:")
  for topping in toppings:
    print(f"- {topping}")

make_sandwich('ham','cheese')
make_sandwich('tomato','lettuce')
make_sandwich('Onions')
