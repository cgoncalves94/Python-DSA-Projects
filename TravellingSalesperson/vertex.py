# Define a Vertex class
class Vertex:
    # Initialize the vertex with a value and an empty dictionary for edges
    def __init__(self, value):
        self.value = value
        self.edges = {}
    
    # Method to add an edge from this vertex to another vertex
    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight
    
    # Method to get all the edges connected to this vertex
    def get_edges(self):
        return list(self.edges.keys())
    
    # Method to get the weight of an edge connecting this vertex to another vertex
    def get_weight(self, edge):
        return self.edges[edge]
