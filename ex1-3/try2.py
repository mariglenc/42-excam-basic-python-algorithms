
def pattern_tracker(text: str) -> int:
    count = 0 # declare the counter of adj nr

    for i in range(len(text)-1): # iterate over the range of text leng - 1 so the index is correct from o to the last one not one more
        if text[i].isdigit() and text[i+1].isdigit(): # make sure they are all digits
            if int(text[i]) + 1 == int(text[i+1]): # make sure the firs digit +1 is == to the next digit
                count += 1 # if so counter + 1
    return count # return total coutner

print(pattern_tracker("01234567"))      # 7
print(pattern_tracker("1234567890"))    # 8  
print(pattern_tracker("987654321"))  # 0
print(pattern_tracker("12a34"))  # 2