# Check if the string is palindrome or not
s = input('Enter a string: ')
if s.lower() == s[::-1].lower():
    print('Palindrome')
else:
    print('Not a Palindrome')
