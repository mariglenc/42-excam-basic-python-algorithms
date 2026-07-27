# ex2-2 - mirror_matrix
# attempt: try8.py
# (signature pre-filled from the .en; write your solution below)

def mirror_matrix(matrix: list[list[int]]) -> list:
    reversed_matrix = [] # declare a empty list
    for list_int in matrix: # iterate over all lists of matrix list
        reversed_matrix.append(list_int[::-1]) # reverse all lists of matrix and append to the revered matrix variable 
    return reversed_matrix # return it
