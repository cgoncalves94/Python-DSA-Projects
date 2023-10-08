# Blossom Project: A HashMap Implementation

## Description

This project, named 'Blossom', focuses on implementing a simple hash map in Python. It leverages a custom linked list data structure to manage collisions within the hash map. The project serves as an example of how to combine different data structures for specific needs.

## Objectives

- **Hash Map Implementation**: Create a custom hash map to store key-value pairs.
- **Linked List Utility**: Utilize a linked list for handling hash map collisions.
- **Method Definitions**: Create methods for hash computation, insertion, retrieval, and deletion.

## How It Works

1. **HashMap Class**: Defines a hash map with methods for common operations like `insert`, `retrieve`, and `delete`.
    - `hash()`: Computes a hash code for a given key.
    - `compress()`: Compresses the hash code to fit within the array size.
    - `assign()`: Adds a key-value pair to the hash map.
    - `retrieve()`: Retrieves a value by key from the hash map.
    - `delete()`: Removes a key-value pair from the hash map.
    - `print_indexes()`: Prints the key-value pairs stored at each index of the hash map's array. Useful for debugging and understanding the hash map's internal state.

2. **Linked List**: A custom linked list implementation is used for each bucket in the hash map to handle collisions.

3. **Blossom Library**: Contains predefined flower definitions as key-value pairs.

4. **Testing**: Creates a HashMap instance and performs various operations to demonstrate its functionality.

## Running the Code

1. Make sure Python is installed on your machine.
2. Clone the repository.
3. Run `script.py`.



