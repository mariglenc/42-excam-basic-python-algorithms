# ex2-2 - mirror_matrix
# attempt: try3.py
# (signature pre-filled from the .en; write your solution below)

def mirror_matrix(matrix: list[list[int]]) -> list:
    reversed = []
    for listt in matrix:
        reversed.append(listt[::-1])
    return reversed
