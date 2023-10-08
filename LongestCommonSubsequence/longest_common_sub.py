dna_1 = "ACCGTT"
dna_2 = "CCAGCA"

def longest_common_subsequence(string_1, string_2):
    print("Finding longest common subsequence of {0} and {1}".format(string_1, string_2))

    cols = len(string_1) + 1
    rows = len(string_2) + 1

    grid = [[0 for col in range(cols)] for row in range(rows)]

    for row in range(1, rows):
        print("Comparing: {0}".format(string_2[row - 1]))
        for col in range(1, cols):
            print("Against: {0}".format(string_1[col - 1]))
            if string_1[col - 1] == string_2[row - 1]:
                grid[row][col] = grid[row - 1][col - 1] + 1
            else:
                grid[row][col] = max(grid[row - 1][col], grid[row][col - 1]) 
    for row_line in grid:
        print(row_line)
    # Extract the LCS string from the grid
    lcs_string = extract_subsequence(grid, string_1, string_2)
    return len(lcs_string), lcs_string

    

def extract_subsequence(grid, string_1, string_2):
    col = len(string_1)
    row = len(string_2)
    lcs = []
    
    # Traverse the grid starting from the bottom-right
    while col > 0 and row > 0:
        if string_1[col - 1] == string_2[row - 1]:
            lcs.append(string_1[col - 1])
            col -= 1
            row -= 1
        else:
            if grid[row - 1][col] > grid[row][col - 1]:
                row -= 1
            else:
                col -= 1

    # Return the reversed LCS since we built it from end to start
    return ''.join(lcs[::-1])

result_length, result_string = longest_common_subsequence(dna_1, dna_2)
print("Length of LCS:", result_length)
print("LCS String:", result_string)




