# SkyRoute - Vancouver Metro Route Finder

## Description
SkyRoute is a Python-based application designed to help users find the shortest metro route between various landmarks in Vancouver. It employs graph search algorithms like Breadth-First Search (BFS) and Depth-First Search (DFS) to find the optimal path.

## Features
- Landmark Choices: Provides a list of popular landmarks in Vancouver for users to select as start and end points.
- Dynamic Routing: Utilizes BFS to find the shortest metro route between the selected landmarks.
- Maintenance Mode: Employs DFS to identify alternative routes when certain metro stations are under maintenance.

## Concepts Applied
- Graph Algorithms: Both BFS and DFS are used for finding routes.
- Data Structures: Utilizes dictionaries and sets to represent the metro system and landmarks.
- Conditional Logic: Includes logic to handle various conditions like maintenance, invalid inputs, and same start-end points.
- User Interaction: Interactive Command Line Interface for a more engaging user experience.

## Output
The program generates textual output listing the sequence of metro stations that form the shortest route between the chosen landmarks. It also provides options for the user to discover another route or exit the application.
