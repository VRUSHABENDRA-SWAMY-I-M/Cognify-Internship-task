def is_palindrome(input_string):
    # Remove spaces and convert to lowercase (optional)
    cleaned_string = input_string.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage:
input_str = input("enter the string:")
if is_palindrome(input_str):
    print(f"{input_str} is a palindrome.")
else:
    print(f"{input_str} is not a palindrome.")
