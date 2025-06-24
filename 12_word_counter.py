text = input("Enter a string: ")
word = input("Enter the word to count: ")

count = text.split().count(word)

print(f"The word '{word}' occurs {count} time(s) in the string.")
