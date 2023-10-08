import utils
import sorts
import time  # Import time module for performance measurement

# Define constant for small CSV filename
SMALL_CSV = 'books_small.csv'

# Comparison functions
def by_title_ascending(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
    return book_a['author_lower'] > book_b['author_lower']

# Function to print sorted books
def print_sorted_books(bookshelf, sort_type, attribute):
    print(f"Sorted by {attribute} using {sort_type}:")
    for book in bookshelf:
        print(book[attribute])

# Test both bubble sort and quicksort on the small dataset
for sort_func, sort_name in [(sorts.bubble_sort, 'Bubble Sort'), (sorts.quicksort, 'Quick Sort')]:
    # Capture the start time
    start_time = time.time()

    # Load bookshelf for testing
    bookshelf = utils.load_books(SMALL_CSV)

    # Sort by title
    if sort_name == 'Quick Sort':
        sort_func(bookshelf, 0, len(bookshelf) - 1, by_title_ascending)
    else:
        sort_func(bookshelf, by_title_ascending)

    # Capture the end time and compute the elapsed time
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Print sorted titles and elapsed time
    print_sorted_books(bookshelf, sort_name, 'title')
    print(f"Time taken for {sort_name} (by title): {elapsed_time:.10f} seconds")

    # Capture the start time
    start_time = time.time()

    # Load another bookshelf for testing
    bookshelf = utils.load_books(SMALL_CSV)
    
    print("------")

    # Sort by author
    if sort_name == 'Quick Sort':
        sort_func(bookshelf, 0, len(bookshelf) - 1, by_author_ascending)
    else:
        sort_func(bookshelf, by_author_ascending)

    # Capture the end time and compute the elapsed time
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Print sorted authors and elapsed time
    print_sorted_books(bookshelf, sort_name, 'author')
    print(f"Time taken for {sort_name} (by author): {elapsed_time:.10f} seconds")

    print("------")
