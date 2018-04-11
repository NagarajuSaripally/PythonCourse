def add(n1, n2):
    print(n1+n2)

add(10,20) #it prints 30

result = 0
try:
    result = 10 + "10"
except:
    print("Hey it looks there is an error")


print(result)


# we can only specify a specific type of error.
#like TypeError, WriteError, OSERROR etc
# finally block executes always no matter what


def ask_for_int():
    while  True:
        try:
            result = int(input('please provide integer: '))
        except:
            print("Whoops! Not a number")
            continue
        else:
            print("Yes Thanks you")
            break
        finally:
            print("End of try except finally, will always run at the end")

ask_for_int()