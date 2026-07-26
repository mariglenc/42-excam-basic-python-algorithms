# arr = [1, 2, 3, 4, 5]

# STEP 1: shrink k with modulo
# k = 1 -> 1 % 5 = 1
# (1 is smaller than 5, so remainder is just 1 -> no shrinking needed here)
# modulo only matters when k >= len, e.g. k=6 -> 6 % 5 = 1 (same as rotating by 1)

# STEP 2: the two slices
# arr[-1:]  -> [5]         the LAST 1 item (the tail that wraps to the front)
# arr[:-1]  -> [1,2,3,4]   EVERYTHING EXCEPT the last 1 (the head that follows)

# STEP 3: glue them, tail first
# arr[-1:] + arr[:-1]
# [5]      + [1,2,3,4]
# = [5, 1, 2, 3, 4]

# RESULT: rotated right by 1 -> the 5 jumped from the end to the front

def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:              # if the input list is empty
        return []            # return an empty list (also avoids dividing by zero below)
    k = k % len(arr)         # shrink k with modulo
    return arr[-k:] + arr[:-k]   # take the last k items, put them in front of the rest