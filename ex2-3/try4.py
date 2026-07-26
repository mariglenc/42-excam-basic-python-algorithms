# ex2-3 - shadow_merge
# attempt: try4.py
# (signature pre-filled from the .en; write your solution below)

def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    merged = []
    for i in range(max(len(list1),len(list2))): # iterate over the range of max len of 1 or 2 (who is bigger)
        if i < len(list1): # if there are items yet
            merged.append(list1[i]) # append in merged
        if i < len(list2): # next one if there is items yet
            merged.append(list2[i]) # also append
    return merged # return list

