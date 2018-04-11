"""
Handle the exception thrown by the code below by using try and except blocks.
for i in ['a','b','c']:
    print(i**2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-c35f41ad7311> in <module>()
      1 for i in ['a','b','c']:
----> 2     print(i**2)

TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
"""

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Please check the type, and enter only integers")
except:
    print("For all other errors")


#Problem 2

"""
Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
x = 5
y = 0

z = x/y
"""

try:
    x = 5
    y = 0
    z = x/y
    print(z)
except:
    print("Any number should not divide by zero")
finally:
    print("All Done.")


#problem 3:

"""
Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
"""

def ask():
    while True:
        try:
            result = int(input("Please enter an integer: "))
            print(result ** 2 )
        except:
            print("Exception occured, you should enter only integers")
            continue
        else:
            print("Above is the square value of your integer, Thanks!")
            break
        finally:
            print("If incorrect, please enter integer else good bye!")

ask()