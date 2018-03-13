"""
Just print the arithmetic operations results of two integers using python language
"""

# addition opeartor + 
print ("addition opeartor + : " + str(2 + 3))

# subtraction operator -
print ("subtraction opeartor - : " + str( 6 - 4))

# multiplication operator *
print ("multiplication opeartor * : " + str(8 * 5))

# division operator /
print ("division opeartor / : " + str( 7 / 9))

# mod operator %
print ("mod opeartor % : " + str( 21 % 2))


"""
Performing arithmetic opeartions using variables
"""

my_income = 500
my_taxes = 0.15
my_taxes_due = my_income * my_taxes;

print("Total Tax due: " + str(my_taxes_due))


"""
Pythone programming language supports dynamic typing which means we don't need to specify the
variable which type it is when we are declaring and intializing the variable. (like javascript)
"""

hello_world = "Hello, World";

print(hello_world); # here it displays the string Hello, World

hello_world = 26;

print(hello_world); # Here as be initialized the hello_world with integer 26 it display 26 (different type)


"""
In Python lanaguage to determine the type of variable there is an inbuilt method called 'type', we can use it
"""

my_current_job = "Software Engineer"

print(type(my_current_job));  # ans : <class 'int'>