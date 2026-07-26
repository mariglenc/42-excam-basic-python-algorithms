# ex1-5 - whisper_cipher
# attempt: try7.py
# (signature pre-filled from the .en; write your solution below)

def whisper_cipher(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a')) # find poisiotn add shift bring back to original position and add a
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A')) # find poisiotn add shift bring back to original position and add a
        else:
            result += char
    return result
