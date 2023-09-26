favorite_places = {
  'bobby' : ['uranus', 'paris'],
  'kenny' : ['jupiter', 'kenya', 'hawaii'],
  'rob' : ['kennys moms house']
}

for name, places in favorite_places.items():
  print(f"\n{name.title()}'s favorite places are:")
  for place in places:
    print(f"\t{place.title()}")