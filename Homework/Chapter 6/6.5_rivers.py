rivers = {
  "nile" : "egypt",
  "mississippi" : "united states",
  "amazon" : "south america",
}

for river, country in rivers.items():
  print(f"\nThe {river.title()} river runs through {country.title()}.")

for river in rivers.keys():
  print(f"\n{river.title()}")

for country in rivers.values():
  print(f"\n{country.title()}")