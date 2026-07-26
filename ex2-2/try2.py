# ex2-2 - mirror_matrix
# attempt: try2.py
# (signature pre-filled from the .en; write your solution below)

def mirror_matrix(matrix: list[list[int]]) -> list:
    reversed = []
    for row in matrix:
        reversed.append(row[::-1])
    return reversed
