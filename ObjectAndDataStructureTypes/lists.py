'''
Lists holds different type of objects in a sequencial orders.
'''

#some mixed lists:

my_lists = [4,5,6]

my_lists = ["stringtype", 6.4, 1]

# slicing and indexing works like strings, also we can concatenate the lists

print(my_lists[0])

print(my_lists[1:])

print(my_lists[1:2])

# concatenation

my_second_list = [10,11,12]

print( my_lists + my_second_list )


# Not like string we can change the lists objects (mutate)

my_lists[0] = 99

print(my_lists)

# to add a new item to the list at the end, we have built in method is called `append`

my_lists.append('this gets added')

print(my_lists)

# to remove the item from the list, removes end of the list if we dont specify , we have built in method is called `pop`

my_lists.pop()

print (my_lists)

print(my_lists.pop(2))

print(my_lists)


# if we wanna sort the objects in the lists, we can use the built in method called sort()

my_lists_two = ['a', 'y', 'l', 'm', 'z', 'w', 'd']

my_lists_three = [10, 3, 1, 4, 5, 2, 9, 6]

my_lists_two.sort()

my_lists_three.sort()

print(my_lists_two)

print(my_lists_three)

'''
None type, if we don't assign anything specific to a variable, type for a None object. To indicate no value, or we can
use as a placeholder.
'''


#reverse
my_lists_three.reverse()

print(my_lists_three)