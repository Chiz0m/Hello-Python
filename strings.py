# strings are easy yet can cause errors if you don't know how to handle them

# short strings with single qoutes
text_single = 'Python is dope'

# short text with double qoutes
text_double = "Python is dope"

# long text with tripple qoutes
text_tripple = ''' 
    Hi Chizom, I just want to send this email saying that
    I like what you are doing with your time. Lol.
    Yeah...
 '''
# print(text_tripple)

# we also have square brackets for strings e.g
text = 'The new me is dope'
print(text)  # this outputs all the text above
print(text[0])  # this outputs only the letter T
print(text[1])  # this outputs only the letter h
print(text[-1])  # this outputs only the letter e. This is called negative index
print(text[0:3])  # this outputs only the letters T h e
print(text[1:])  # this outputs all the letters and leaves out the letter T
print(text[:])  # this outputs all the letters
print(text[2:0])  # this outputs nothing
