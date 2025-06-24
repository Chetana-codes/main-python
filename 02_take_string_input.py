# Accept string input from the user
user_input = input("Enter a string: ")

# Initialize counters
digit_count = 0
letter_count = 0

# Loop through each character in the string
for char in user_input:
    if char.isdigit():
        digit_count += 1
    elif char.isalpha():
        letter_count += 1

# Display the results
print("Number of letters:", letter_count)
print("Number of digits:", digit_count)
