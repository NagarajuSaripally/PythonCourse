#1 Lesser of Two evens : write a function that returns the lesser of two given numbers if both numbers are even, but returns
# greater if one or both numbers are odd.

def lesser_of_two_evens(num1, num2):
	if num1 % 2 == 0 and num2 % 2 == 0:
		if num1 >= num2:
			return num2
		else:
			return num1
	else:
		if num1 >= num2:
			return num1
		else:
			return num2

print(f'Lesser of two even numbers: {lesser_of_two_evens(12,3)}')



# Animal Crackers: write a function takes a two word string and returns True if both words begin with same letter

def animal_crackers(string):
	my_string = string.split(' ')
	if my_string[0][0] == my_string[1][0]:
		return True
	else:
		return False

print(f'Animal Cracker: {animal_crackers("Levelheaded Llama")}')

# Makes twenty: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not,
# return False

def makes_twenty(num1, num2):
	if num1 == 20 or num2 == 20 or (num1 + num2) == 20:
		return True 
	else:
		return False

print(f'Makes twenty with 20, 18 {makes_twenty(20, 18)}')
print(f'Makes twenty with 12, 8 {makes_twenty(12, 8)}')
print(f'Makes twenty with 13, 21 {makes_twenty(13, 21)}')