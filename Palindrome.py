def is_palindrome(text):
    text = text.lower()          # make it case-insensitive
    return text == text[::-1]    # reverse and compare

word = input("Enter a word: ")

if is_palindrome(word):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
