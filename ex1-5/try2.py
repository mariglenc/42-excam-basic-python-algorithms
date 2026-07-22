
def whisper_cipher(text: str, shift: int) -> str:
    result = "" # declare the result var
    for char in text: # iterate over all chars
        if 'a' <= char <= 'z': # if it is a lowercase letter
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a')) 
            # ord(char) - convert char to ordinate
            # - ord('a') - minus ordinate of a
            #  + shift - we add that also shift
            #  % 26 - we divede it to 26 and get the reminder of it
            # + ord('a') - we add the ordinate of a to the reminder
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char # if not a letter just add the char
    return result


print(whisper_cipher("Hello, World!", 3))  # Output: "Khoor, Zruog!"
print(whisper_cipher("Abz", 3))  # Output: "Dec"
print(whisper_cipher("WXYZ 1", 1))  # Output: "YZAB 1"
             