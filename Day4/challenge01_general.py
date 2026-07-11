#check if number is even
'''
def is_even(num):
    return num % 2 == 0
    
number = int(input("Enter a number: "))
result = is_even(number)
if result == True:
    print(f"{number} is a Even Number")
else:
    print(f"{number} is a Odd Number")

#reverse_string(text)
def reverse_string(text):
    reversed_string = ""
    for i in text[::-1]:
        reversed_string += i
    return reversed_string

def is_palindrome(text):
    text = text.lower()
    return text == reverse_string(text)
       
text = input("Enter a String: " )
print(reverse_string(text))
print(is_palindrome(text))
'''
#Challenge 3 find max number

def find_max(numbers):  
    max_num = numbers[0]  
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

numbers = [12, 45, 78, 123, 99, 56]
print(find_max(numbers))