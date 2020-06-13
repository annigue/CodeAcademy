destinations = ["Paris, France", "Shanghai, China","Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index


def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = traveler.index(traveler_destination)
  return traveler_destination_index


# defining a list of attractions
attractions = [[] for i in destinations]

print(attractions)

def add_attraction(destination, attraction):
  global destination_index
  try:
    destination_index = get_destination_index(destination)
  except:
    return destination_index
  attractions.insert(destination_index,attraction)
  return attractions

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for i in attractions_in_city:
     possible_attraction = i
     attractions_tags = i[1]
     for interest in interests:
        if (interest in attractions_tags):
          attractions_with_interest.append(possible_attraction)
  return attractions_with_interest

#comment

la_arts = find_attractions("Los Angeles, USA", ["art"])
print(la_arts)