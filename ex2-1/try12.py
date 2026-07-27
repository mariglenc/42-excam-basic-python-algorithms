# ex2-1 - echo_validator
# attempt: try12.py
# (signature pre-filled from the .en; write your solution below)

def echo_validator(text: str) -> bool:
    cleaned = ""
    for char in text:
        if char.isalnum():
            cleaned += char.lower()

    return cleaned == cleaned[::-1]

