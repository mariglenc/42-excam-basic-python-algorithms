# ex1-4 - string_sculptor
# attempt: try10.py
# (signature pre-filled from the .en; write your solution below)

def string_sculptor(text: str) -> str:
    result = ""
    i = 0
    for char in text:
        if char.isalpha(): # make sure is letter    
            print(i)
            if i % 2 == 0: # first letter
                result += char.lower()
            else: # second letter
                result += char.upper()
            i += 1 # incrfease only for letters
        else:
            result+=char # leave as it is non letters
    return result


print(string_sculptor("Hello"))