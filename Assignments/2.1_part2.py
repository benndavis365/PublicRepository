print("Welcome!")
company = input("What is the nmame of your company? ")
cable_in_ft = input("How much fiber optic cable will be neede in feet? ")
cable_in_ft = int(cable_in_ft)

if cable_in_ft > 500:
  total_cost = cable_in_ft * .50
  print(f"Your total cost for {company.title()} is ${total_cost}")
elif cable_in_ft > 250:
  total_cost = cable_in_ft * .70
  print(f"Your total cost for {company.title()} is ${total_cost}")
elif cable_in_ft > 100:
  total_cost = cable_in_ft * .80
  print(f"Your total cost for {company.title()} is ${total_cost}")
else:
  total_cost = cable_in_ft * .87
  print(f"Your total cost for {company.title()} is ${total_cost}")
