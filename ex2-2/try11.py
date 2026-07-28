# ex2-2 - mirror_matrix
# attempt: try11.py
# (signature pre-filled from the .en; write your solution below)

def mirror_matrix(matrix: list[list[int]]) -> list:
    revesed_lists = []
    for each_list in matrix:
        revesed_lists.append(each_list[::-1])
    return revesed_lists
