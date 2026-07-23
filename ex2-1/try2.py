
def echo_validator(text: str) -> bool:
    cleaned = "" # decalre a cleaned var which has only letter and numbers
    for char in text: # iterate over all chars of the text
        if char.isalnum(): # only for letters and numbers
            cleaned += char.lower() # convet them all to lowercase very important
    return cleaned == cleaned[::-1] # compare the cleaned word with the reversed version of it


print(echo_validator("A man, a plan, a canal: Panama"))   #-> True
print(echo_validator("racecar")                       )   #-> True
print(echo_validator("hello")                         )   #-> False
print(echo_validator("")                              )   #-> True
