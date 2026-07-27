# ex2-2 - mirror_matrix
# attempt: try5.py
# (signature pre-filled from the .en; write your solution below)

def mirror_matrix(matrix: list[list[int]]) -> list:
    reversed = []
    for list in matrix:
        reversed.append(list[::-1])
    return reversed
