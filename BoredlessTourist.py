destinations = ["Paris, France", "Shanghai, China","Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return(destination_index)


def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = traveler.index(traveler_destination)
  return(traveler_destination_index)


# defining a list of attractions
attractions = [[] for i in destinations]

#print(attractions)

 
def add_attraction(destination, attraction):
 destination_index = get_destination_index(destination)
 try:
   destination_index = get_destination_index(destination)
   attractions_for_destination = attractions[destination_index]
   attractions_for_destination.append(attraction)
 except SyntaxError:
   return
 attractions_for_destination = attractions[destination_index] 
  

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
  for attri in attractions_in_city:
    possible_attraction = attri
    attractions_tags = attri[1]
    for interest in interests:
      if interest in attractions_tags:
      	attractions_with_interest.append(possible_attraction[0])
  return(attractions_with_interest)
  
def get_attractions_for_traveler(traveler):
	 traveler_destination = traveler[1]
	 traveler_interests = traveler[2]
	 traveler_attraction = find_attractions(traveler_destination, traveler_interests)
	 interests_string = str("Hi "+ traveler[0] + ", we think you'll like these places around ")
	 for each in traveler_attraction:
	 	interests_string = interests_string + traveler_destination + str(": ") + str(each)
	 return(interests_string)
	 
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
 
 

la_arts = find_attractions("Los Angeles, USA", ['art'])
#print(la_arts)
