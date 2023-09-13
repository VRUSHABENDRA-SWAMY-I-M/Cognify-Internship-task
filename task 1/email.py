import re

def is_valid_email(email):
    # Define a regular expression pattern for a valid email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use the re.match() function to match the pattern against the email
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage:
email = input("enter the email:")
if is_valid_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")
