from cs50 import get_string

text = get_string("Text: ")
letters = 0
words = 1
sentences = 0
for i in range(len(text)):
    if text[i].isalpha():
        letters += 1
    if text[i] == ' ':
        words += 1
    if text[i] == '.' or text[i] == '!' or text[i] == '?':
        sentences += 1
Let = (letters / words) * 100
Set = (sentences / words) * 100
index = round((0.0588 * Let) - (0.296 * Set) - 15.8)
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print("Grade ", index)