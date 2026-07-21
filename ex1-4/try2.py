
def string_sculptor(text: str) -> str:
    result="" # declare the resul
    i = 0 # declare the index for letters only

    for char in text: # iterate over text chars
        if char.isalpha(): # if char is letter 
            if i % 2 == 0: # if index of letter is even
                result += char.lower() # make it lowercase
            else: 
                result += char.upper() # if index is not even make it uppercase
            i += 1 # increase index + 1 for letters
        else:
            result += char # else add the other types of char into result
    return result # return it

print(string_sculptor("Heeelllo/123 World"))

