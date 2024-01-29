def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

# Test the function
word = input("Lütfen bir kelime giriniz: ")
if is_palindrome(word):
    print(f"{word} , bir palindromdur")
else:
    print(f"{word} ,palindrom değildir.")
