# ex1-5 - whisper_cipher
# attempt: try12.py
# (signature pre-filled from the .en; write your solution below)

def whisper_cipher(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(
                (ord(char) - ord('a') + shift) # find poistion and add shift
                % 26  # if more than z bring to inital positio n
                + ord('a') # convert to a real letter position
            )
        elif 'A' <= char <= 'Z':
            result += chr(
                (ord(char) - ord('A') + shift) # find poistion and add shift
                % 26  # if more than z bring to inital positio n
                + ord('A') # convert to a real letter position
            )
        else:
            result += char
            
    return result

