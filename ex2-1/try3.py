# ex2-1 - echo_validator
# attempt: try3.py
# (signature pre-filled from the .en; write your solution below)

def echo_validator(text: str) -> bool:
    cleaned = "" # decalre a var for only text nums
    for char in text: # iterate over all chars on the txt string
        if char.isalnum():
            cleaned += char.lower()
    return cleaned == cleaned[::-1]
