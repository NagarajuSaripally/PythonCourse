'''
Tuples are also immutable, we cannot alter values once we intiate them
Tuples are added through ()

The main reason to use Tuples to maintain the `Data Integrity`
'''

tpl = (1,2,3)

print(tpl);

print(type(tpl))

# it can have a mix type

tpl1 = (1, 'string', 2.5)

print(tpl1)

#built in methods:

#count : displays the count of repeated character or value

tpl2 = ('a', 'b', 'c', 'a')

print(tpl2.count('a'))

#index : first time appeared index location

print(tpl2.index('a'))