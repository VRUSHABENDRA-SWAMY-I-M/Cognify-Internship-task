def reverse_string(input_string):
    
    reversed_string = input_string[::-1]
    return reversed_string

input_str = input("enter the string:")
result = reverse_string(input_str)
print(result) 