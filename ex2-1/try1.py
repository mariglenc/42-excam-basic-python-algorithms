
def echo_validator(text: str) -> bool:
    # declare a cleaned var where we make all them lowercase
    cleaned = ""
    for char in text: # iterate over all text 
        if char.isalnum(): # just the letters or numbers
            cleaned += char.lower() # convert all them in lowercase
 
    return cleaned == cleaned[::-1] # return true if the normal one is the same as the reversed one

print(echo_validator("hello"))  # Output: False
print(echo_validator("abc"))    # Output: False
print(echo_validator("ma dam"))  # Output: True
print(echo_validator("1 23 21"))  # Output: True
print(echo_validator("12345"))  # Output: False 