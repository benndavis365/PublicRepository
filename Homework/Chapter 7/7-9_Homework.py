sandwich_orders = ['pastrami','meat lovers','pastrami','veggie','pastrami','sweet & spicy']
finished_sandwiches = []

print("Oh no! We've run out of pastrami")

while 'pastrami' in sandwich_orders:
  sandwich_orders.remove('pastrami')

while sandwich_orders:
  sandwich_order = sandwich_orders.pop()
  print(f"\nMaking {sandwich_order.title()} sandwich")
  finished_sandwiches.append(sandwich_order)

# Display all finished orders
print("\nThe following sandwiches have been made:")
for sandwich_order in finished_sandwiches:
  print(sandwich_order.title())