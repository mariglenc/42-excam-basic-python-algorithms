
def string_sculptor(text: str) -> str:
    result = "" # decalre an empty result
    i = 0       # declare an index to find the letter order for cases

    for char in text: # iterate over the text chars
        if char.isalpha(): # if char is letter
            if i % 2 == 0: # if letter is even
                result = result + char.lower() # make it lowercase
            else:
                result = result + char.upper() # else make it uppercase
            i = i +1 # increase index only for letters
        else:
            result = result + char # else add the other chars into result

    return result

print(string_sculptor("Heeelllo/123 World"))
