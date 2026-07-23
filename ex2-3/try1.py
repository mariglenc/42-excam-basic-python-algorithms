
def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    merged = [] # declare a new list to merge both lists into it
    for i in range(max(len(list1),len(list2))):
        