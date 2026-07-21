
def pattern_tracker(text: str) -> int:
    count = 0 # decalre the count for adjacent nr

    for i in range(len(text) - 1): # iterate by index, stopping one before the end so i+1 stays valid
        if text[i].isdigit() and text[i+1].isdigit(): # make sure each index is digit otherwise go to the next one
            if int(text[i]) + 1 == int(text[i+1]): # if the digits are fisrt digit + 1 == next digit then increase counter  
                count = count + 1
    
    return count


print(pattern_tracker("01234567"))      # 7
print(pattern_tracker("1234567890"))    # 8  
print(pattern_tracker("987654321"))  # 0
print(pattern_tracker("12a34"))  # 2