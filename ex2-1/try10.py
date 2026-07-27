# ex2-1 - echo_validator
# attempt: try10.py
# (signature pre-filled from the .en; write your solution below)

def echo_validator(text: str) -> bool:
    cleaned = "" # declare the empty string for cleaned chars
    for char in text: # iterate over all chars
        if char.isalnum(): # get all nums and letters
            cleaned += char.lower() # add them to cleaned var in lowercase

    return cleaned == cleaned[::-1] # compare the cleaned version with the reversed same [::-1]

