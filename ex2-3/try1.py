
def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    merged = [] # declare a new list to merge both lists into it
    for i in range(max(len(list1),len(list2))):
        if i < len(list1): # if list1 has still elements 
            merged.append(list1[i]) # append into merged
        if i < len(list2): # if next one of list2 jast sitll elements
            merged.append(list2[i]) # append to merged

    return merged

print(shadow_merge([1, 2, 3], [4, 5, 6]))  # Output: [1, 4, 2, 5, 3, 6]
print(shadow_merge([1, 2], [3, 4, 5, 5, 4, 3, 2, 1]))  # Output: [1, 3, 2, 4, 5, 5, 4, 3, 2, 1]