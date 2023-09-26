prompt = "Please enter a pizza topping you'd like to add to your pizza "
prompt += "\n Please type 'quit' when finished: "

while True:
  topping = input(prompt)

  if topping == 'quit':
    break
  else:
    print(f"I'dd add {topping.title()} to your pizza!")
