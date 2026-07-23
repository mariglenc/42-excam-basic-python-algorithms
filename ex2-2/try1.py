
def mirror_matrix(matrix: list[list[int]]) -> list: # list[list[int]] -> a list where each item is a list of ints.
    result = [] # declare the result of the reversed lists
    for row in matrix: # eaterate over each nested list of all matrix lists
        result.append(row[::-1]) # reverse each nested list and append to the result list
    return result # return it after fully insterd all

print(mirror_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))   # -> [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
print(mirror_matrix([[1, 2], [3, 4]]))                    # -> [[2, 1], [4, 3]]
print(mirror_matrix([[1, 2, 3, 4, 5]]))                   # -> [[5, 4, 3, 2, 1]]   (single row)
print(mirror_matrix([[7], [8], [9]]))                     # -> [[7], [8], [9]]     (single-column rows: reversing a 1-item row changes nothing)
print(mirror_matrix([]))                                  # -> []                  (empty matrix)
print(mirror_matrix([[1, 2, 3]]))                         # -> [[3, 2, 1]]
print(mirror_matrix([[10, 20], [30, 40], [50, 60]]))      # -> [[20, 10], [40, 30], [60, 50]]