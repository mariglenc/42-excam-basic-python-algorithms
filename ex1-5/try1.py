
def whisper_cipher(text: str, shift: int) -> str:
    result = "" # declare a result var
    for char in text: # iterate over all chars of the text
        if 'a' <= char <= 'z': # if  char is letter and lowercase
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a')) # shift the letter: map to 0–25, add shift, wrap with %26, map back to a letter
        elif 'A' <= char <= 'Z': # if char is letter and uppercase
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A')) # shift the letter: map to 0–25, add shift, wrap with %26, map back to a letter
        else:
            result += char # otherwise add char
    
    return result


print(whisper_cipher("Hello, World!", 3))  # Output: "Khoor, Zruog!"
print(whisper_cipher("Abz", 3))  # Output: "Dec"
print(whisper_cipher("WXYZ 1", 1))  # Output: "YZAB 1"
            