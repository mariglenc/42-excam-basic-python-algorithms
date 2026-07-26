# ex1-5 - whisper_cipher
# attempt: try10.py
# (signature pre-filled from the .en; write your solution below)

def whisper_cipher(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(
                (ord(char) - ord('a') + shift) % 26 + ord('a') # find position and add shift, if is beyound z fix position and conver back to real letter
            )
        elif 'A' <= char <= 'Z':
            result += chr(
                (ord(char) - ord('A') + shift) % 26 + ord('A') # find position and add shift, if is beyound z fix position and conver back to real letter
            )
        else:
            result += char
    return result

