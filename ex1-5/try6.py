# ex1-5 - whisper_cipher
# attempt: try6.py
# (signature pre-filled from the .en; write your solution below)

def whisper_cipher(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(
                (ord(char) - ord('a') + shift) # find position and shift
                % 26 # if bigger than z than bring back to a 
                +ord('a') # and reminder add again to the ord of a
            )
        elif 'A' <= char <= 'Z':
            result += chr(
                (ord(char) - ord('A') + shift) # find position and shift
                % 26 # if bigger than z than bring back to a 
                +ord('A') # and reminder add again to the ord of a
            )
        else:
            result += char
    return result
