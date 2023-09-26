prompt = "Welcome to the movies! How old are you: "
age = input(prompt)
age = int(age)
while True:
    if age < 3:
      price = 0
    elif age <= 12:
      price = 10
    else:
      price = 15

    print(f"The ticket price for your age is ${price}.")
    break