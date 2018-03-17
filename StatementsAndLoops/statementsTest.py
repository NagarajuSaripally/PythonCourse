print("Question 1:")

'''
Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
'''

st = 'Print only the words that start with s in this sentence'

list_worlds = st.split(' ')

for word in list_worlds:
	if word[0] == 's':
		print(word)

print('\n')

print("Question 2:")

'''
Use range() to print all the even numbers from 0 to 10.

'''

for num in range(0, 11):
	if num%2 == 0:
		print(num)

listOfNums = list(range(0,11,2))
print(listOfNums)

print('\n')


print("Question 3:")
'''
Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
'''

my_list = [ num for num in range(1, 50) if num%3 == 0 ]

print(my_list)

print('\n')

print('Question 4:')

'''
Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
'''

st = 'Print every word in this sentence that has an even number of letters'

words = st.split(' ')

for word in words:
	if len(word) % 2 == 0 :
		print(word + 'is even!')

print("Another Approch")

myList = [word for word in st.split(' ') if len(word) % 2 == 0]

print(myList)

print('\n')


print('Question 5:')

'''
Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
'''

nums = range(1, 101)

for num in nums:
	if num % 3 == 0 and num % 5 == 0 :
		print('FizzBuzz')
	elif num % 3 == 0:
		print('Fizz')
	elif num % 5 == 0:
		print('Buzz')
	else:
		print(num)

print('\n')


print('Question 6:')

'''
Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
'''

st = 'Create a list of the first letters of every word in this string'

my_list = [ letter[0] for letter in st.split(' ')]
print(my_list)