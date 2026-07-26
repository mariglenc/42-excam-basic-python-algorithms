# ex1-4 - string_sculptor
# attempt: try4.py
# (signature pre-filled from the .en; write your solution below)

def string_sculptor(text: str) -> str:
    i = 0
    result = ""
    for char in text:
        if char.isalpha():
            if i % 2 == 0:
                result += char.lower()
            else:
                result += char.upper()
            i += 1
        else:
            result+=char
    return result