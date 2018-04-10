"""
__name__ is a built in variable, this variable name is gets assigned as a string when we run the python file using Python command

if we run direct from command line, python will assign __name = "__main__"

then we can check using if condition.
if __name__ == "__main__":
"""

import one

print("Top level in two.py")

one.func()

if __name__ == '__main__':
    print("Two.py runs directly")
else:
    print("Two.py has been imported")