
# The Bored Tourist Project

## Description

This project, named 'The Bored Tourist', is designed to help travelers find attractions that match their interests in various global destinations. It makes use of Python lists and functions to manage traveler data and attractions.

## Objectives

- **List Management**: Utilize Python lists to store destinations and attractions.
- **Function Definitions**: Create functions to manage traveler data, find attractions, and provide personalized recommendations.
- **Data Structuring**: Learn how to structure data in nested lists and how to access this data.

## How It Works

1. **Destinations List**: Holds a list of available destinations in the format "City, Country".
2. **Attractions List**: A nested list initialized based on the destinations list, where each sub-list corresponds to a destination and contains attractions for that destination.
3. **Test Traveler Data**: Sample traveler data used for testing. Includes traveler's name, destination, and interests as a list. The format is ["Name", "Destination City, Country", ["interest1", "interest2", ...]].
4. **Function Definitions**: 
   - `get_destination_index()`: Finds the index of a given destination in the destinations list.
   - `get_traveler_location()`: Retrieves the current location of a traveler.
   - `add_attraction()`: Adds an attraction to the appropriate destination.
   - `find_attractions()`: Finds attractions that match a traveler's interests in a given destination.
   - `get_attractions_for_traveler()`: Provides a personalized list of attractions for a traveler based on their interests and destination.

## Tests

- **Test Case 1**: This test aims to validate the function `find_attractions` by checking if it returns the correct list of art attractions in Los Angeles.
- **Test Case 2**: This test aims to validate the function `get_attractions_for_traveler` by checking if it returns a personalized message listing all attractions in Shanghai, China that match Erin Wilkes' interests.

