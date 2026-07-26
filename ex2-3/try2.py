# ex2-3 - shadow_merge
# attempt: try2.py
# (signature pre-filled from the .en; write your solution below)

def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    joined = []
    max_len = max(len(list1), len(list2)) 
    for i in range(max_len):
        if i < len(list1):
            joined.append(list1[i])
        if i < len(list2):
            joined.append(list2[i])
    return joined



print(shadow_merge([1,2,3], [4,5,6]))     # [1,4,2,5,3,6]
print(shadow_merge([1,2], [3,4,5,6]))     # [1,3,2,4,5,6]
print(shadow_merge([], [1,2,3]))          # [1,2,3]
print(shadow_merge([1,2,3], []))          # [1,2,3]