# range(). --> it prints specified range but not the includes the specified number

for num in range(10):
	print(num)

# range(0,10,2)  0 is begining of the range, 10 is end of the range and 2 is the steps that needs to consider
for num in range(0,10,2):
	print(f'with step 2 : {num}')

print('\n')
'''
Enumerate:
built in enumerate()

enumarate helps to calculate the index counter and stores that value in a specified variable at that particular index
it returns tuples
'''

print('\n')
print("enumerate() operator -> generator")

word = 'abcde'

for item in enumerate(word):
	print(item)

print('\n')
'''
zip() : opposite of enumrates, zip together two lists

'''
print('\n')
print("ZIP() operator -> generator")
my_list = [1,2,3]
my_list_2 = ['a','b','c'];

for item in zip(my_list, my_list_2):
	print(item)

print('\n')

'''
in -> checks whether the compared item in the lists or dictionaries or in strings
'''

print('\n')
print("in. operator -> generator")
print('\n')

print('a' in [1,2,3,])

print('x' in 'Hello world')

print('key' in {'key': 'hello world'})


# min and max methods

print('\n')
print("min and max functions -> prints min and max numbers in a list")
print('\n')

my_list = [10,20,30,40,50]

print(min(my_list))

print(max(my_list))


'''
Importing libraries:
'''

from random import shuffle

my_another_list = [1,2,3,4,5,6,7,8,9]

shuffle(my_another_list)

print(f'Shuffled list: {my_another_list}')


from random import randint

print(randint(0, 100))


'''
input: gives user option to enter a value
input always retuns in a string formate, if we wanna convert to integer or float, there is int() and float()
'''

result = input('what is your name? ')

print(result)


'''

List comprehension: 
'''
word = 'hello'
my_list = []

for letter in word:
	my_list.append(letter)

print(my_list)

# instead of appending this characters into the my_list we can use "list comprehension" concept like below
# letter and letter should match


word1 = "Hello World"
my_list2 = [letter for letter in word1]
print(my_list2)


# we can perform operation on the first variable in the list comprehension

my_list_3 = [num**2 for num in range(0,11)]
print(my_list_3)



# we can also add if condition in this comprehension which is

my_list_4 = [num**2 for num in range(0, 11) if num%2 == 0]

print(my_list_4)