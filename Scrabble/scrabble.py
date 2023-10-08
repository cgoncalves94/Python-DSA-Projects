
# Scrabble Scoring Exercise

# Define a list of uppercase alphabets
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Define corresponding points for each alphabet
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Create a dictionary to map each letter to its corresponding points
letter_to_points = {letter: point for letter, point in zip(letters, points)}

# Add space character with 0 points
letter_to_points[" "] = 0

# Function to calculate the total points for a given word
def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter.upper(), 0)
    return point_total

# Testing the function
# Test 1: Calculating points for the word 'BROWNIE'
print("Points for BROWNIE:", score_word("BROWNIE"))

# Test 2: Calculating points for the word 'PYTHON'
print("Points for PYTHON:", score_word("PYTHON"))
