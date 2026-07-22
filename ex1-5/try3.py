def whisper_cipher(text: str, shift: int) -> str:
    result = "" # decalre result variable
    for char in text: # iterate over all chars of the text
        if 'a' <= char <= 'z':
            result += chr(
                (ord(char) - ord('a') + shift) # ord(z) 122 - ord(a) 97 + 10 -> is beound alphabet
                % 26 + ord('a') # in this case we divide and get the reminder + ord(a)
            ) # so then we convert again the result int to character
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char # else add the char to it
    return result


print(whisper_cipher("Hello, World!", 3))  # Output: "Khoor, Zruog!"
print(whisper_cipher("Abz", 3))  # Output: "Dec"
print(whisper_cipher("WXYZ 1", 1))  # Output: "YZAB 1"
             