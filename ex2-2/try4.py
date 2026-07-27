# ex2-2 - mirror_matrix
# attempt: try4.py
# (signature pre-filled from the .en; write your solution below)

def mirror_matrix(matrix: list[list[int]]) -> list:
    reversed = []
    for int_list in matrix:
        reversed.append(int_list[::-1])
    return reversed
