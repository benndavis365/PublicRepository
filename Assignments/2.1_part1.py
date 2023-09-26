print("Welcome!")
company = input("What is the nmame of your company? ")
cable_in_ft = input("How much fiber optic cable will be neede in feet? ")
cable_in_ft = int(cable_in_ft)

final_cost = cable_in_ft * .87

print(
    f"Your company is {company.title()} and the total cost for the cable is ${final_cost} "
)
