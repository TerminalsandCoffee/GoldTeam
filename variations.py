#Using Python String Methods

message = input("Enter a message: ")


print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Captitalized:", message.capitalize())
print("Title case:", message.title())

words = message.split()
print("Words:", words)

sorted_words = sorted(words)
print("Alphabetic First Word: ", sorted_words[0])
print("Alphabetic Last Word: ", sorted_words[-1])
