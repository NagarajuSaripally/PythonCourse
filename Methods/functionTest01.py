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



'''
level 1:
'''

# old Macdonald: write a function that capitalizes the first and fouth letters of a name

def old_macdonald(name):
	newName = ''
	for index, x in enumerate(name):
		if index == 0 or index == 3:
			newName += x.upper()
		else:
			newName += x.lower()
	return newName;

print(f'Old Macdonald: Make 1 and 4 the charactrer upper case: {old_macdonald("macdonald")}')
print(f'Old Macdonald: Make 1 and 4 the charactrer upper case: {old_macdonald("stevejobs")}')


# master Yoda: given a sentence, return a sentence with the words reversed.
def master_yoda(sentence):
	return " ".join(sentence.split(' ')[::-1])

print(f'Master yoda: {master_yoda("I am home")}')
print(f'Master yoda: {master_yoda("we are ready")}')


# almost There : given an integer n, return True if n is within 10 of either 100 or 200

#Method 1:

def almost_there(num):
	return num in range(90, 111) or num in range(190, 211)

#method 2:

def almost_there_2(num):
	if (90 <= num <=110) or (190 <= num <= 210):
		return True
	else:
		return False

print(f'Almost There: 90 --> {almost_there(90)}')
print(f'Almost There: 104 --> {almost_there(104)}')
print(f'Almost There: 150 --> {almost_there(150)}')
print(f'Almost There: 209 --> {almost_there(209)}')
print(f'Almost There: 90 --> {almost_there_2(90)}')
print(f'Almost There: 104 --> {almost_there_2(104)}')
print(f'Almost There: 150 --> {almost_there_2(150)}')
print(f'Almost There: 209 --> {almost_there_2(209)}')

























