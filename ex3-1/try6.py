# ex3-1 - twist_sequence
# attempt: try6.py
# (signature pre-filled from the .en; write your solution below)

def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
        return []
    k = k % len(arr)
    return arr[-k:] + arr[:-k]
