# ex1-3 - pattern_tracker
# attempt: try3.py
# (signature pre-filled from the .en; write your solution below)

def pattern_tracker(text: str) -> int:
    count = 0
    for i in range(len(text) -1 ):
        if text[i].isdigit() and text[i+1].isdigit():
           if int(text[i]) + 1 == int(text[i+1]):
               count += 1

    return count 

print(pattern_tracker("12345"))   # -> 4   # (1,2)(2,3)(3,4)(4,5)
print(pattern_tracker("a1b2") )   # -> 0   # digits are not adjacent
print(pattern_tracker("9012") )   # -> 2   # (0,1)(1,2)
print(pattern_tracker("abc")  )   # -> 0
print(pattern_tracker("")     )   # -> 0