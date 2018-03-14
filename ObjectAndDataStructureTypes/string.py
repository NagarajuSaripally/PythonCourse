'''
* strings are ordered sequences
* We can also use rever indexing in Python like other programming lanugages
* slice -> [start:stop:step]
* start : the slicing that going to start
* stop : the slicing upto but not included.
* step : size of the jump that we take from start to stop
'''

# single quotes
print('Hello World!')

# double quotes
print("Hello World!")

# escape sequences
print('Hello \n World!')


'''
There is method in the python that gives the length of string
Sytax : len('string')  --> 6
'''

my_string = "Hello World!, new to Python."

lengthOfMyString = len(my_string)

print("Length of my string :" + str(lengthOfMyString));


# String Indexing:

# to print W from the my_string
print(my_string[6])

#to print last character of my_string
print(my_string[-1])


'''
Slicing the string Python
'''

#starting index
print(my_string[2:])

#stop index (don't include specified index)
print(my_string[:3])

#to print the sub section of the string
print(my_string[2:6])

# to display the whole string from all the way begenning to end, we can do in two ways
# approach 1
print(my_string)

# approach 2.  // reason : step size not mentioned
print(my_string[::])


# if we mention the step size it displays the index characters based on the step size
print(my_string[::2]) #result --> HloWrl!
print(my_string[::3]) #result --> Hlod


#to reverse the string in the python we can use this jump negative trick
print(my_string[::-1]) #result --> prints result in negative.


'''
String Property and Methods

* string are immutable in python, we cannot replace the indexes of string with other values
'''

# string concatenation
print ("Hello World " + "it is beautiful outside")

# string mutliplication
print ('z' * 10)


'''
Built-in string methods, there are so many built in string function, out of them few of the functions with example below
'''

wish = "Good Evening"

#upper case
print (wish.upper())

#lower case
print (wish.lower())

#split
print (wish.split())


'''
String formatting with printing, there are multiple ways to do that
'''

#string interpolation

print("Hello " + wish)

# formatting with format method
'''
pros: insert the string the same formate that we pass them
      and we can position them based on the indexes
'''

print("This is a string {}".format('that we inserted'))


print("The {} {} {}".format('fox', 'brown', 'quick')) # result -> the fox brown quick


#we can also print them in a way that we want using indexing
print("The {2} {1} {0}".format('fox', 'brown', 'quick')) # result -> the quick brown fox


#we can also repease the same string with the same index
print("The {2} {2} {0}".format('fox', 'brown', 'quick')) # result -> the quick quick fox


#we can also use the keywords instead of indexes (like alias name)
print("The {q} {b} {f}".format(f='fox', b='brown', q='quick')) # result -> the quick brown fox



'''
Float number formatting
'''
result = 100/999

print("The floating result {}".format(result))

# in order to display the anticipated precision value we can use this string format with following syntax
# {value:width.precision f}

print("The floating point result {r:1.4f}".format(r=result))  #result -->   x.yyyy


'''
Formating string literals
'''

name = "John Doe"
 
print(f"Hello his name is {name}")  #new in python 3.6 or higher

# works with multiple variables too

firstName = "John"
lastName = "Doe"
age = "26"

print(f'His name is {firstName}, {lastName} and his age is {age}')
