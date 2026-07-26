
def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:              # if the input list is empty
        return []            # return an empty list (also avoids dividing by zero below)
    k = k % len(arr)         # if k is bigger than the list, keep only what's left after full turns
    return arr[-k:] + arr[:-k]   # take the last k items, put them in front of the rest

# Example usage:
print(twist_sequence([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
print(twist_sequence([1, 2, 3, 4, 5], 3))  # Output: [3, 4, 5, 1, 2]
print(twist_sequence([1, 2, 3, 4, 5], 5))  # Output: [1, 2, 3, 4, 5]