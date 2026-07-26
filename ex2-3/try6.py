# ex2-3 - shadow_merge
# attempt: try6.py
# (signature pre-filled from the .en; write your solution below)

def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    merged = []
    for i in range(max(len(list1),len(list2))):
        if i < len(list1):
            merged.append(list1[i])
        if i < len(list2):
            merged.append(list2[i])
    return merged