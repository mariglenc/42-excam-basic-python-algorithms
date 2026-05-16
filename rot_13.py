def rot_13(s):
	result = ""
	for char in s:
		if ('A' <= char <= 'M'):
			result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
		elif ('N' <= char <= 'Z'):
			result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
		elif ('a' <= char <= 'm'):
			result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
		elif ('n' <= char <= 'z'):
			result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
		else:
			result += char
	return result

# Example usage:
print(rot_13("Hello, World!"))  # Output: "Uryyb, Jbeyq!"
print(rot_13("Uryyb, Jbeyq!"))  # Output: "Hello, World!"