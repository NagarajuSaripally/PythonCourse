
# Numbers: Numerical values, either integiers or float point values

# stings : collection of characters in an order, usually specified wrap them inside either '', or "" EX: "This is a string"

# Lists : sequence of ordered objects and lists are mutable, []

# Tuples : sequence of ordered objects, but tuples are imputable

# dictionaries : sequence of unordered objects, save data in key pair values


'''
Numbers:
'''

#1 : Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

equation = (((2 * 10)/2)**2) + 1.25 - 1

print('1) The equation (((2 * 10)/2)**2) + 1.25 - 1 is equals to : {}'.format(equation))

#2 Answers to the following questions

print('2a) What is the value of the expression 4 * (6 + 5) -> my answer : {}, computed answer : {}'.format(44, 4 * (6 + 5)))
print('2b) What is the value of the expression 4 * 6 + 5 -> my answer : {}, computed answer: {}'.format(29, 4 * 6 + 5))
print('2c) What is the value of the expression 4 + 6 * 5 -> my answer : {}, computed answer: {}'.format(34, 4 + 6 * 5))


#3 What is the type of the result of the expression 3 + 1.5 + 4?
# My answer : Float
typeOfequation = type(3+1.5+4);
print('3) What is the type of the result of the expression 3 + 1.5 + 4? : {}'.format(typeOfequation))

#4 What would you use to find a number’s square root, as well as its square?

print('4a) square root: 100 ** 0.5 -> {}'.format(100 ** 0.5))

print('4b) square : 10 ** 2 -> {}'.format(10 ** 2))


'''
Strings:
'''

#1 Given the string 'hello' give an index command that returns 'e'
# s = 'hello'

s = 'hello'

print('1) Given the string "hello" give an index command that returns "e" : Answer -> s[1] -> {}'.format(s[1]))


#2 Reverse the string "hello" using slicing:

s = 'hello'[::-1]

print('2) Reverse the string "hello" using slicing: : Answer -> "hello"[::-1] -> {}'.format(s))


#3 Given the string hello, give two methods of producing the letter 'o' using indexing.

print('3a) Given the string hello, give two methods of producing the letter "o" using indexing. Method 1) -> "hello"[-1] -> {}'.format("hello"[-1]))

print('3b) Given the string hello, give two methods of producing the letter "o" using indexing. Method 2) -> "hello"[4:] -> {}'.format("hello"[4:]))

'''
Lists
'''

#1 Build this list [0,0,0] two separate ways.
# Method 1
listMethod_1 = [0,0,0]

#Method 2

listMethod_2 = []

listMethod_2.append(0)
listMethod_2.append(0)
listMethod_2.append(0)

print(listMethod_1)
print(listMethod_2)

#Method 3

listMethod_3 = [0]*3

print(listMethod_3)


#2 : Reassign 'hello' in this nested list to say 'goodbye' instead:

list3 = [1,2,[3,4,'hello']]

list3[2][2] = 'goodbye'

print(list3)


#3 Sort the list below:

list4 = [5,3,4,6,1]

list4.sort()

print(list4)



'''
Dictonaries:
'''

#1  Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key':'hello'}

print('1) d["simple_key"] -> {}'.format(d["simple_key"]))


#2 Grab 'hello'=

d = {'k1':{'k2':'hello'}}

print('2) d["k1"]["k2"] -> {}'.format(d["k1"]["k2"]))


#3 Getting a little tricker -> #Grab hello
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print('3) d["k1"][0]["nest_key"][1][0] -> {}'.format(d["k1"][0]["nest_key"][1][0]))

#4 This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print('4) d["k1"][2]["k2"][1]["tough"][2][0] -> {}'.format(d["k1"][2]["k2"][1]["tough"][2][0]))



'''
Tuples are immutable where lists are mutable
Creation of tuples
'''

tpl = ('1','2','3')

print(tpl);


'''
Sets
'''
list5 = [1,2,2,33,4,4,11,22,3,3,2]

list5 = set(list5)

print('sets -> {}'.format(list5))



'''
Boolean:
'''

print('Question 2 > 3 : myAnswer -> {}, computed-value : {}'.format('False', 2 > 3))
print('Question 3 <= 2 : myAnswer -> {}, computed-value : {}'.format('False', 3 <= 2))
print('Question 3 == 2.0 : myAnswer -> {}, computed-value : {}'.format('False', 3 == 2.0))
print('Question 3.0 == 3 : myAnswer -> {}, computed-value : {}'.format('True', 3.0 == 3))
print('Question 4**0.5 != 2 : myAnswer -> {}, computed-value : {}'.format('False', 4**0.5 != 2))


l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]


print('Question l_one[2][0] >= l_two[2]["k1"] : myAnswer -> {}, computed-value : {}'.format('False', l_one[2][0] >= l_two[2]['k1']))