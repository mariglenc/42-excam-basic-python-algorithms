# ex2-3 - shadow_merge
# attempt: try7.py
# (signature pre-filled from the .en; write your solution below)

def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    merged = []
    for i in range(max(len(list1),len(list2))): # iterate over max length of one of the lists
        if i < len(list1): # if list1 has items yet
            merged.append(list1[i]) # append
        if i < len(list2):
            merged.append(list2[i])

    return merged
