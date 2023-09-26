cities = {
  "dallas": {
    "country": "united states",
    "population": "2 million peeps",
    "fact": "insert fact here",
  },
  "fort worth": {
    "country": "united states",
    "population": "3 million peeps",
    "fact": "insert fact here",
  },
  "austin": {
    "country": "united states",
    "population": "1 million peeps",
    "fact": "insert fact here",
  },
}

for city, city_info in cities.items():
  print(f"\nCity: {city.title()}")
  country = city_info['country']
  population = city_info['population']
  fact = city_info['fact']

  print(f"\tCountry: {country.title()}")
  print(f"\tPopulation: {population.title()}")
  print(f"\tFact: {fact.title()}")