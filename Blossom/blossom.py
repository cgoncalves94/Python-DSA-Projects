from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 

# Blossom Project: A HashMap Implementation in Python

# HashMap Class Definition
class HashMap:
    # Constructor: Initializes the hash map with a given size.
    def __init__(self, size):
        self.array_size = size
        self.array = [None for _ in range(self.array_size)]
    
    # Hash Function: Takes a string and returns a hash code.
    def hash(self, key):
        return sum(key.encode())
    
    # Compression Function: Compresses the hash code to fit within the array size.
    def compress(self, hash_code):
        return hash_code % self.array_size
    
    # Assign Method: Adds a key-value pair to the hash map.
    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        if self.array[array_index] is None:
            self.array[array_index] = LinkedList()
        self.array[array_index].insert(Node([key, value]))
    
    # Retrieve Method: Retrieves the value for a given key from the hash map.
    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]
        
        # Type check: proceed only if list_at_index is a LinkedList object
        if not isinstance(list_at_index, LinkedList):
            return None  # Return None to indicate key not found
        
        current = list_at_index.get_head_node()
        while current:
            if current.get_value()[0] == key:
                return current.get_value()[1]
            current = current.get_next_node()
        return None  # Return None to indicate key not found


    
    # Delete Method: Deletes a key-value pair from the hash map.
    def delete(self, key):
        array_index = self.compress(self.hash(key))
        self.array[array_index] = None

    # String Representation Method: Provides a string representation of the hash map.
    def __repr__(self):
        return "{0}".format(self.array)
    
    # Print Indexes Method: Prints the key-value pairs at each index of the hash map's array.
    def print_indexes(self):
        for i, linked_list in enumerate(self.array):
            print(f"Index {i}:", end=" ")
            if linked_list is None:
                print("None")
            else:
                current = linked_list.get_head_node()
                while current:
                    print(f"{current.get_value()} -> ", end="")
                    current = current.get_next_node()
                print("None")
    

# Initialize HashMap
blossom = HashMap(len(flower_definitions))

# Populate HashMap
for flower, meaning in flower_definitions:
    blossom.assign(flower, meaning)

# Print HashMap
blossom.print_indexes()

# User Interface: Retrieve flower definitions based on user input.
while True:
    new_flower = input("Enter a flower name (or type 'exit' to quit): ").lower()
    
    # Exit condition
    if new_flower == 'exit':
        print("Goodbye!")
        break
    
    # Retrieve flower meaning
    meaning = blossom.retrieve(new_flower)
    if meaning:
        print("The meaning of {0} is {1}".format(new_flower, meaning))
    else:
        print("Flower not found.")





