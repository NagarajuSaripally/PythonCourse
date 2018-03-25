'''
Dictionaries are unordered sequence objects, instead of sequence oder they store in key and value pair.
Like objects in javascript and java lanugage

when can we use lists and Dictionaries:

Dictionaries: not able to sort and objects retrieved by key name

Lists : Objects retrieved based by location
'''

my_dictionary = {
	'firstname' : 'Jone',
	'lastname' : 'Doe'
}

# to print whole dictionary:

print(my_dictionary);

# to print specific value

print(my_dictionary['firstname'])

groceries_prices = {
	'fruits' : {
		'bananas' : 2.99,
		'orenge' : 0.99,
		'mango' : 1.49
	},
	'vegetebles' : {
		'cucumber' : 1.99,
		'califlower' : [2.99, 3.99],
		'potato' : 4.99	
	} 
}

print(groceries_prices);

print('fruits are {}'.format(groceries_prices['fruits']))

print('califlower prices are {}'.format(groceries_prices['vegetebles']['califlower']))


# to add a new dictionary value to a existing dictionary:

d = {'k1' : 100, 'k2' : 200}

print(d)

d['k3'] = 300

print(d)

# to get all keys
print(d.keys())

# to get all values
print(d.values())

# to get both keys and values called items
print(d.items()) # it returns tuples which are in paranthesis ()