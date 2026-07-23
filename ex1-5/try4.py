
def whisper_cipher(text: str, shift: int) -> str:
    result = "" # declare the var result to return
    for char in text: # iterate over all chars of string text
        if 'a' <= char <= 'z': # check if it is lowercase letter
            result += chr( 
                (ord(char) - ord('a')   # what position is this letter? (a=0, b=1, ... z=25)
                + shift)                # move it forward
                % 26                    # if it went past z, loop back to a
                + ord('a')              # turn the position back into a real letter
            )
        elif 'A' <= char <= 'Z':
            result += chr(
                (ord(char) - ord('A')   # what position is this char
                + shift)                # move forward shift times
                % 26                    # if is bigger than Z loop back to A
                + ord('A')              # turn the positon back into a real letter
            )
        else:
            result += char # else if is not letter just add that to the result
    return result



print(whisper_cipher("abc", 1))            # -> "bcd"
print(whisper_cipher("xyz", 3))           # -> "abc"
print(whisper_cipher("Hello, World!", 13)) # -> "Uryyb, Jbeyq!"
print(whisper_cipher("ABC", -1))           # -> "ZAB"
