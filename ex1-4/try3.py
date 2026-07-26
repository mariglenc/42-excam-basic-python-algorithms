# ex1-4 - string_sculptor
# attempt: try3.py
# (signature pre-filled from the .en; write your solution below)

def string_sculptor(text: str) -> str:
    alternated = ""
    i = 0
    
    for char in text:
        if char.isalpha():
            if i % 2 == 0:
                alternated += char.lower()
            else:
                alternated += char.upper()
            i += 1
        else:
            alternated += char
    return alternated