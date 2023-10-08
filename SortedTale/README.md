# A Sorted Tale: Performance Comparison of Sorting Algorithms

## Description

This project, named 'A Sorted Tale,' aims to compare the performance of different sorting algorithms, specifically bubble sort and quick sort, using Python. It uses a dataset of books and sorts them by various attributes, such as title and author.

## Objectives

- **Algorithm Implementation**: Implement bubble sort and quick sort algorithms.
- **Data Sorting**: Sort a dataset of books by title and author.

## How It Works

1. **Sorting Algorithms**: The `sorts.py` file contains the implementations of bubble sort and quick sort algorithms.
    - `bubble_sort()`: Sorts an array using bubble sort.
    - `quicksort()`: Sorts an array using quick sort.

2. **Utility Functions**: The `utils.py` file provides utility functions for loading books from a CSV file.
    - `load_books()`: Loads books into a list of dictionaries.

3. **Main Script**: The `scripts.py` file serves as the driver code to execute sorting and performance measurement.
    - `by_title_ascending()`: Comparison function to sort by title.
    - `by_author_ascending()`: Comparison function to sort by author.

## Running the Code

1. Make sure Python is installed on your machine.
2. Clone the repository.
3. Run `scripts.py`.

### Output

The script will print out:
- Sorted books by title and author.
- Average time taken for bubble sort and quick sort to sort the books by title and author.



