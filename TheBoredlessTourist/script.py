
# Function to find the index of a destination in the 'destinations' list
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

# Function to get the location index of a traveler based on their destination
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


# Function to add an attraction to the relevant destination
def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions[destination_index].append(attraction)
    except ValueError:
        return

# Function to find attractions at a given destination based on interests
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for possible_attraction in attractions_in_city:
        attraction_tags = possible_attraction[1]  
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
                return attractions_with_interest

# Function to get attractions for a traveler based on their interests
def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interests_string = "Hi "
    interests_string += traveler[0]
    interests_string += ", we think you'll like these places around "
    interests_string += traveler_destination

    for i in range(len(traveler_attractions)):
        if traveler_attractions[-1] == traveler_attractions[i]:
            interests_string += "the " + traveler_attractions[i] + "."
        else:
            interests_string += "the " + traveler_attractions[i] + ";"
    return interests_string

#Test the code

# List of destination cities available with the travel agency, each as a string in the format "City, Country".
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]


# Initialize an empty list of attractions for each destination. 
# Each index corresponds to the destination at the same index in the 'destinations' list.
attractions = [[] for _ in destinations]


# Populate the 'attractions' list with sample attractions for each destination.
# Each attraction is a list containing its name and a list of its types (e.g., ['beach', 'museum']).
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# Sample traveler data used for testing. Includes traveler's name, destination, and interests as a list.
# Format: ["Name", "Destination City, Country", ["interest1", "interest2", ...]]
test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]
print(test_traveler)

# Test Case 1: Find all art-related attractions in Los Angeles, USA.
# This test aims to validate the function find_attractions by checking if it returns the correct list of art attractions in Los Angeles.
la_arts = find_attractions("Los Angeles, USA", ["art"])
print(la_arts)

# Test Case 2: This test aims to validate the function get_attractions_for_traveler by checking if it returns a personalized message listing all attractions in Shanghai, China that match Erin Wilkes' interests.
get_attractions_test  = get_attractions_for_traveler(test_traveler)
print(get_attractions_test)


