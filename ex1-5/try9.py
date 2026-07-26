# ex1-5 - whisper_cipher
# attempt: try9.py
# (signature pre-filled from the .en; write your solution below)

def whisper_cipher(text: str, shift: int) -> str:
    shifted = ""
    for char in text:
        if 'a' <= char <= 'z':
            shifted += chr(
                (ord(char)-ord('a')+shift) # find position of the char and add the shift nr
                % 26 # wraps back to the start if we passed 'z' (keeps the position within 0-25)
                + ord('a') # convert the position number back into a real letter
            )
        elif 'A' <= char <= 'Z':
            shifted += chr(
                (ord(char)-ord('A')+shift) # find position of the char and add the shift nr
                % 26 # wraps back to the start if we passed 'z' (keeps the position within 0-25)
                + ord('A') # convert the position number back into a real letter
            )
        else:
            shifted += char
    return shifted








# ord('a') = 97
# ord('f') = 102
# ord('z') = 122
# f 102 - a 97 + 10 ->15 % 26 = 15 + 97 