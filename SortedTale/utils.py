import csv
import os

def load_books(filename):
    bookshelf = []

    # Determine the current directory and build the path to the data file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(current_dir, filename)

    with open(data_file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            row['title_lower'] = row['title'].lower()
            row['author_lower'] = row['author'].lower()
            bookshelf.append(row)
            
    return bookshelf
