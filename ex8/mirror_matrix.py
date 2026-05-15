def mirror_matrix(matrix: list[list[int]]) -> list:
    result = []
    for row in matrix:
        result.append(row[::-1])
    return result
