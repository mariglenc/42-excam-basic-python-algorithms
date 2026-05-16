def is_palindrome(text: str):
    cleaned = ""
    
    for char in text:
        if char.isalnum():  # vetëm shkronja dhe numra
            cleaned += char.lower()
    
    return cleaned == cleaned[::-1]
# Example usage:
print(is_palindrome("A man a plan a canal Panama"))  # Output: True
print(is_palindrome("Hello"))  # Output: False
print(is_palindrome("an a")) # Output: True
print(is_palindrome("No 'x' in Nixon"))  # Output: True
print(is_palindrome("12321"))  # Output: True
