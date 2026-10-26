# Day-07: Basic String Programs
text = input("Enter a string: ")
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Reversed:", text[::-1])
print("Vowel count:", sum(1 for ch in text.lower() if ch in "aeiou"))

# Sample Output (input: python):
# Enter a string: python
# Length: 6
# Uppercase: PYTHON
# Lowercase: python
# Reversed: nohtyp
# Vowel count: 1
