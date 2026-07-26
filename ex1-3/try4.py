# ex1-3 - pattern_tracker
# attempt: try4.py
# (signature pre-filled from the .en; write your solution below)

def pattern_tracker(text: str) -> int:
    count = 0
    for i in range(len(text) - 1):
        if text[i].isdigit() and text[i+1].isdigit(): # if is digit
            if int(text[i]) + 1 == int(text[i+1]): # if previous [i] + 1 is equal with next one [i+1]
                count += 1 # increase counter

    return count
