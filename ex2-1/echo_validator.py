def echo_validator(text: str) -> bool:
    clean = ""
    for char in text:
        if char.isalnum():
            clean += char.lower()
    return clean == clean[::-1]
