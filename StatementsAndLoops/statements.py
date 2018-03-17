"""
States are used to control the flow of the programming, we can see few keywords for these statements below
if, elif, else

syntax:
in Pythong the colon and indentation is crusial, it allows the code more readable and understandable

if someCondition:
	#if condition code here
elif:
	#else if condition code here
else:
	else code here
"""

#if statement:

if True:
	print("Yai this true")

#if else statement:

hungry = False

if hungry:
	print("I am hungry, feed me")
else:
	print("I not hungry, don't feed me")

#if elif else statement: just to explain, time is in integers and in 24 format

time = 18

if(time < 11):
	print("It is morning!, good morning!")
elif(time>=12 and time<=15):
	print("It is afternoon!")
elif(time>=16 and time<=20):
	print("It is evening!")
else:
	print("It is night, good night!");