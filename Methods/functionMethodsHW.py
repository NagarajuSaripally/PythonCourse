# Write a function that computes the volume of a sphere given its radius.
# Formula ((4/3) * 3.14) * r ** 3


def vol(radius):
	return ((4/3) * 3.14) * (radius ** 3)

print(f'Volume of a sphere with radius 2 --> {vol(2)}')
print(f'Volume of a sphere with radius 5 --> {vol(5)}')
print(f'Volume of a sphere with radius 10 --> {vol(10)}')


# Write a function that checks whether a number is in a given range(inclusive of high and low)

def ran_check(num,low,high):
	if num in range(low, high+1):
		print(f'{num} is in the range between {low} and {high}')


def ran_bool(num, low, high):
	return (num in range(low, high+1))


ran_check(5, 2, 7)
print(f'Is 5 in range between 2 and 7: --> {ran_bool(5,2,7)}')

# write a python function that accepts a string and caulcuates the number of upper case letter and lower case letters.

def up_low(string):
	upper = 0
	lower = 0
	for character in string:
		if character.isupper():
			upper += 1
		elif character.islower():
			lower += 1
	print(f'No. of upper case characters: {upper}')
	print(f'No. of lower case characters: {lower}')

print(f'Original String: Hello Mr. Rogers, how are you this fine Tuesday? --> {up_low("Hello Mr. Rogers, how are you this fine Tuesday?")}')

# write a python function that takes a list and returns a new list with unique elem,ents of the first list.
# sample list: [1,1,1,1,2,2,3,3,3,3,4,5]

def unique_list(lst):
	return list(set(lst))

print(f'Unique List of: [1,1,1,1,2,2,3,3,3,3,4,5] --> {unique_list([1,1,1,1,2,2,3,3,3,3,4,5])}')


#method 2: without built in method:

def unique_list_2(lst):
	unique_list1 = []
	for item in lst:
		if not item in unique_list1:
			unique_list1.append(item)
	print(unique_list1)

unique_list_2([1,1,1,1,2,2,3,3,3,3,4,5])


#write a python function to multiply all the numbers in a list.
#sample List : [1,2,3,-4]

def multiply(numList):
	result = 1
	for num in numList:
		result *= num
	return result

print(f'The result of sample List: [1,2,3,-4] is --> {multiply([1,2,3,-4])}')

# write a Python function that checks whether a passed in string is palindrome or not.

def isPalindrome(string):
    string1 = string
    string2 = string[::-1]
    if string1 == string2:
        return True
    return False

print(f'is "helleh" a palindrome --> {isPalindrome("helleh")}')
print(f'is "anna" a palindrome --> {isPalindrome("anna")}')
print(f'is "civic" a palindrome --> {isPalindrome("civic")}')
print(f'is "something" a palindrome --> {isPalindrome("something")}')


# Write a Python function to check whether a string is pangram or not.

# Note: Pangrams are worlds or sentences containing every letter of the alphabet at least once.

# Ex: 'The quick brown fox jumps over the lazy dog'

import string

def ispangram(str1, alphabet=string.ascii_lowercase):  
    alphaset = set(alphabet)  
    return alphaset <= set(str1.lower())

print(f'is Pangram --> {ispangram("The quick brown fox jumps over the lazy dog")}')

