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



'''
Level 2:
'''

# give a list of ints, return Tre if the array contains 3 next to a 3 somewhere:

# means [1,3,3,] --> return True, [1,3,1,3] --> return False


def has_33(myList):
	for index, x in enumerate(myList):
		if index != len(myList) -1:
			if myList[index] == 3 and myList[index+1] == 3 :
				return True
	return False;

print(f'Has_33 in [1,3,3] -> {has_33([1,3,3])}')
print(f'Has_33 in [1,3,1,3] -> {has_33([1,3,1,3])}')
print(f'Has_33 in [3,1,3,] -> {has_33([3,1,3])}')


# paper doll: Given a string, return a string where for every character in the original there are three chracters

def paper_doll(text):
	my_result = ''
	for character in text:
		my_result += character * 3
	return my_result

print(f'Paper Doll: Hello --> {paper_doll("Hello")}')
print(f'Paper Doll: Mississippi --> {paper_doll("Mississippi")}')


# Black Jack: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum
# if their sum exceeds 21 and theres an eleven, redc ue the total sum by 10
# Finally if rthe sume(even after adjustment) exceeds 21 return 'BUST'

def blackjack(num1, num2, num3):
	sumOfNums = num1 + num2 + num3
	if sumOfNums <= 21:
		return sumOfNums
	elif num1 == 11 or num2 == 11 or num3 == 11:
		sumOfNums -= 10
		if sumOfNums > 21:
			return 'BUST'
		else:
			return sumOfNums
	else:
		return 'BUST'


print(f'Black Jack: (5, 6, 7) --> {blackjack(5,6,7)}')
print(f'Black Jack: (9, 9, 9) --> {blackjack(9, 9, 9)}')
print(f'Black Jack: (9, 9, 11) --> {blackjack(9, 9, 11)}')
print(f'Black Jack: (9, 10, 11) --> {blackjack(9, 10, 11)}')
print(f'Black Jack: (11, 10, 11) --> {blackjack(11, 10, 11)}')


#summer of 69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and
#extending to the next 9 (every 6 will be followed by at least 9). return 0 for no numbers

def summer_69(myList):
	_indecisOf6 = []
	_indecisOf9 = []

	for index, x in enumerate(myList):
		if myList[index] == 6:
			_indecisOf6.append(index)
		elif myList[index] == 9:
			_indecisOf9.append(index)
	if len(_indecisOf9) == 0 and len(_indecisOf6) == 0:
		return sum(myList)
	else:
		list1 = myList[0:_indecisOf6[-1]:1]
		list2 = myList[_indecisOf9[0]+1 : len(myList) : 1]
		subList = list1 + list2
		if len(subList) == 0:
			return 0
		else: 
			return sum(subList)

print(f'summer_69 : [1,3,5] --> {summer_69([1,3,5])}')
print(f'summer_69 : [4,5,6,7,8,9] --> {summer_69([4,5,6,7,8,9])}')
print(f'summer_69 : [2,1,6,9,11] --> {summer_69([2,1,6,9,11])}')
print(f'summer_69 : [1,2,3,6,4,6,9] --> {summer_69([1,2,3,6,4,6,9])}')










