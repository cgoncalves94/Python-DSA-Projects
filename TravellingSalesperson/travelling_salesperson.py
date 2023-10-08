# Import required modules and classes
import random
from random import randrange
from graph import Graph
from vertex import Vertex

# Function to print the graph's vertices and their edges
def print_graph(graph):
    for vertex in graph.graph_dict:
        print("")
        print(vertex + " connected to")
        vertex_neighbors = graph.graph_dict[vertex].edges
        if len(vertex_neighbors) == 0:
            print("No edges!")
        for adjacent_vertex in vertex_neighbors:
            print("=> " + adjacent_vertex)

# Function to build the graph for the Travelling Salesperson Problem
def build_tsp_graph(directed):
    g = Graph(directed)
    vertices = []
    # Initialize vertices
    for val in ['a', 'b', 'c', 'd']:
        vertex = Vertex(val)
        vertices.append(vertex)
        g.add_vertex(vertex)
        
    # Add edges between vertices with weights
    g.add_edge(vertices[0], vertices[1], 3)
    g.add_edge(vertices[0], vertices[2], 4)
    g.add_edge(vertices[0], vertices[3], 5)
    g.add_edge(vertices[1], vertices[0], 3)
    g.add_edge(vertices[1], vertices[2], 2)
    g.add_edge(vertices[1], vertices[3], 6)
    g.add_edge(vertices[2], vertices[0], 4)
    g.add_edge(vertices[2], vertices[1], 2)
    g.add_edge(vertices[2], vertices[3], 1)
    g.add_edge(vertices[3], vertices[0], 5)
    g.add_edge(vertices[3], vertices[1], 6)
    g.add_edge(vertices[3], vertices[2], 1)
    return g

# Function to check if all nodes are visited
def visited_all_nodes(visited_vertices):
    for vertex in visited_vertices:
        if visited_vertices[vertex] == "unvisited":
            return False
    return True

# Helper function to find the next vertex to visit
def find_next_vertex(current_vertex, visited_vertices, graph):
    current_vertex_edges = graph.graph_dict[current_vertex].get_edges()
    current_vertex_edges_weights = {}
    for edge in current_vertex_edges:
        current_vertex_edges_weights[edge] = graph.graph_dict[current_vertex].get_weight(edge)
    
    while True:
        if not current_vertex_edges_weights:
            return None
        next_vertex = min(current_vertex_edges_weights, key=current_vertex_edges_weights.get)
        if visited_vertices[next_vertex] == "visited":
            current_vertex_edges_weights.pop(next_vertex)
        else:
            return next_vertex

# Main function to solve the Travelling Salesperson Problem
def traveling_salesperson(graph):
    ts_path = ""
    visited_vertices = {x: "unvisited" for x in graph.graph_dict}
    current_vertex = random.choice(list(graph.graph_dict))
    visited_vertices[current_vertex] = "visited"
    ts_path += current_vertex
    has_visited = visited_all_nodes(visited_vertices)
    
    while not has_visited:
        next_vertex = find_next_vertex(current_vertex, visited_vertices, graph)
        if next_vertex is None:
            has_visited = True
        else:
            current_vertex = next_vertex
            visited_vertices[current_vertex] = "visited"
            ts_path += current_vertex
        has_visited = visited_all_nodes(visited_vertices)
    print(ts_path)


# Build the graph and call the main function
graph = build_tsp_graph(False)
traveling_salesperson(graph)



