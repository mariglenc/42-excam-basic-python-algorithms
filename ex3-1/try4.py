# ex3-1 - twist_sequence
# attempt: try4.py
# (signature pre-filled from the .en; write your solution below)

def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr: # if list array is empty
        return [] # return empty list
    k  = k % len(arr) # shrink k
    return arr[-k:] + arr[:-k] # return the last k elements + the first k elements
