# ex2-2 - mirror_matrix
# attempt: try10.py
# (signature pre-filled from the .en; write your solution below)

def mirror_matrix(matrix: list[list[int]]) -> list:
    reverse_matrix = []
    for lisst in matrix:
        reverse_matrix.append(lisst[::-1])
    return reverse_matrix
