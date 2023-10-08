# Importing required modules and data
from vc_landmarks import vc_landmarks
from vc_metro import vc_metro
from landmark_choices import landmark_choices
from graph_search import bfs, dfs

# Initialization of global variables
landmark_string = ""
stations_under_construction = []

# Functions to greet the user and show available landmarks
def greet():
    global landmark_string
    landmark_string = create_landmark_string(landmark_choices)
    print("Hi there and welcome to SkyRoute!")
    print("We'll help you find the shortest route between the following Vancouver landmarks:")
    print(landmark_string)

def goodbye():
    print("Thanks for using SkyRoute!")

# Function to create a string from landmarks dictionary
def create_landmark_string(choices):
    return "\n".join([letter + " - " + landmark for letter, landmark in choices.items()])

# Function to show landmarks to the user
def show_landmarks():
    see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")
    if see_landmarks == 'y':
        print(landmark_string)

# Function to get active stations
def get_active_stations():
    updated_metro = vc_metro
    for station_under_construction in stations_under_construction:
        for current_station, neighboring_stations in vc_metro.items():
            if current_station != station_under_construction:
                updated_metro[current_station] -= set(stations_under_construction)
            else:
                updated_metro[current_station] = set([])
    return updated_metro

# Function to get the start and end landmarks
def set_start_and_end(start_point, end_point):
    if start_point is not None:
        while True:  # Keep asking until a valid input is received
            change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
            if change_point == 'b':
                start_point = get_start()
                end_point = get_end()
                break  # Exit the loop
            elif change_point == 'o':
                start_point = get_start()
                break  # Exit the loop
            elif change_point == 'd':
                end_point = get_end()
                break  # Exit the loop
            else:
                print("Oops, that isn't 'o', 'd', or 'b'...")
    else:
        start_point = get_start()
        end_point = get_end()
    
    return start_point, end_point

# Function to get the start landmark
def get_start():
    start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
    if start_point_letter in landmark_choices.keys():
        start_point = landmark_choices[start_point_letter]
        return start_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        return get_start()

# Function to get the end landmark
def get_end():
    end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")
    if end_point_letter in landmark_choices.keys():
        end_point = landmark_choices[end_point_letter]
        return end_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        return get_end()

# Function to find a new route based on the given start and end landmarks
def new_route(start_point=None, end_point=None):
    start_point, end_point = set_start_and_end(start_point, end_point)
    if start_point is None or end_point is None:
        print("Invalid start or end point.")
        return
    shortest_route = get_route(start_point, end_point)
    
    if shortest_route is None:
        print("Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(start_point, end_point))
    elif isinstance(shortest_route, str):
        print(shortest_route)
    else:
        shortest_route_string = '\n'.join(shortest_route)
        print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
    
    again = input("Would you like to see another route? Enter y/n: ")
    if again == 'y':
        show_landmarks()
        new_route(start_point, end_point)


# Helper function to check for maintenance conditions
def check_for_maintenance(metro_system, start_stations, end_stations):
    for start_station in start_stations:
        for end_station in end_stations:
            if dfs(metro_system, start_station, end_station) is None:
                return True
    return False

# Helper function to find routes
def find_routes(metro_system, start_stations, end_stations):
    routes = []
    for start_station in start_stations:
        for end_station in end_stations:
            route = bfs(metro_system, start_station, end_station)
            if route:
                routes.append(route)
    return routes

# Function to get the best route
def get_route(start_point, end_point):
    if start_point == end_point:
        return ["You're already at your destination!"]

    start_stations = vc_landmarks.get(start_point, set())
    end_stations = vc_landmarks.get(end_point, set())

    if start_stations == end_stations:
        return ["No need to travel, you're already there!"]

    metro_system = get_active_stations() if stations_under_construction else vc_metro

    if stations_under_construction and check_for_maintenance(metro_system, start_stations, end_stations):
        return "maintenance"

    routes = find_routes(metro_system, start_stations, end_stations)

    if not routes:
        return "No route found."

    return min(routes, key=len)



# Main function to run the program
def skyroute():
    greet()
    new_route()
    goodbye()

# Run the program
skyroute()

