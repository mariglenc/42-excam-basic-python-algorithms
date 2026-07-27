# ex1-3 - pattern_tracker
# attempt: try14.py
# (signature pre-filled from the .en; write your solution below)

def pattern_tracker(text: str) -> int:
    count = 0 # declare a counter of ascending cons nr
    for i in range(len(text) - 1 ): # iterate over the range - 1 because it start from 0 to last
        if text[i].isdigit() and text[i+1].isdigit(): # check if is digit the current and the next i + 1
            if int(text[i])+1 == int(text[i+1]): # cueck if current with index[i] + 1 is equal to the next one with index[i+1]
                count += 1 # if so increase count + 1
    return count
    