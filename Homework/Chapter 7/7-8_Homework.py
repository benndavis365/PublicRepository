sandwich_orders = ['meat lovers','veggie','sweet & spicy']
finished_sandwiches = []

while sandwich_orders:
  sandwich_order = sandwich_orders.pop()
  print(f"Making {sandwich_order.title()} sandwich")
  finished_sandwiches.append(sandwich_order)

# Display all finished orders
print("\nThe following sandwiches have been made:")
for sandwich_order in finished_sandwiches:
  print(sandwich_order.title())