destinations = ["Paris, France", "Shanghai, China","Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

#print(get_destination_index("Bahamas"))


def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = traveler.index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

# defining a list of attractions
attractions = [[] for i in destinations]

print(attractions)

def add_attraction(destination, attraction):
  destination_index = destinations.index(destination)
  try:
    destination_index = destinations.index(destination)
  except SyntaxError:
    return destination_index
  attractions_for_destinations = attraction.append[0]
  return attractions_for_destinations



print(add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']]))