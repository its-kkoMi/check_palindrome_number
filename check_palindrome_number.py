# Assignment 5 - Exercise 9
# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers.

# Ask user for a number

number = int(input("Input a number: "))

# Check if number is a palindrome

def palindrome(number):
    print("\nOriginal Number:", number)
    original_number = number
    
    # Reverse the number
    reverse_number = 0
    while number > 0:
        remainder = number % 10
        reverse_number = (reverse_number * 10) + remainder
        number = number // 10
    
    # Print yes or no if number is palindrome    
    if original_number == reverse_number:
        print("\nThe given number is a palindrome!")
    else:
        print("\nThe given number is not a palindrome!")

palindrome(number)