text = input("Enter text: ")
cleaned = ""

for character in text:
    if character.isalnum():
        cleaned += character.lower()

reversed_text = cleaned[::-1]

if cleaned == reversed_text:
    print("The text is a palindrome.")
else:
    print("The text is not a palindrome.")
