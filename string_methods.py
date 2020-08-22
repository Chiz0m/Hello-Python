# there are methods that can be used with strings
text = 'I am blessed'
print(len(text))  # outpts the number of characters in the text including the spaces
print(text.upper())  # converts the text to upper case
print(text.lower())  # converts the text to lower case
# returns the index where the letter 'a' is positioned in the text
print(text.find('a'))
print(text.replace('am', 'am too'))  # replaces the text 'am' with 'am too'
print(text.title())  # capitalizes the first letter of each character
# returns a boolean value. if am exist in text, a true will be outputed
print('am' in text)
