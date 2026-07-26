# ex2-1 - echo_validator
# attempt: try4.py
# (signature pre-filled from the .en; write your solution below)

def echo_validator(text: str) -> bool:
    cleaned_alnum = ""
    for char in text:
        if char.isalnum():
            cleaned_alnum += char.lower()
    return cleaned_alnum == cleaned_alnum[::-1]
