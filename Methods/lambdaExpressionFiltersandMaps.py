'''
Lambda expressions are quick way of creating the anonymous functions:
'''
#function without lamda expression:

def square(num):
	return num ** 2

print(square(5))

#converting it into lambda expression:

lambda num : num ** 2

#if we want we can assign this to variable like
square2 = lambda num : num ** 2. # we are not going to use this very often, cause lamda function are anonymous

print(square2(5))


print(list(map(lambda num : num **2, [1,2,3,4])))

'''
Map: map() --> map(func, *iterables) --> map object
'''

def square(num):
	return num ** 2

my_nums = [1,2,3,4,5]

#if I wanna get sqaure for all the list items, we can use map function, instead of for loop, for loop is costly

#Method 1:
for item in map(square, my_nums):
	print(item)

#method 2:

list(map(square, my_nums))


def splicer(mystring):
	if len(mystring) % 2 == 0:
		return 'EVEN'
	else:
		return mystring[0]

names = ['andy', 'sally', 'eve']

print(list(map(splicer, names)))


'''
Filter: iterate function that returns either true or false
'''

def check_even(num):
	return num % 2 == 0

my_numbers = [1,2,3,4,5,6]

print(list(filter(check_even, my_numbers)))