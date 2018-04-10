def func():
    print("Func() In ONE.py")

def func1():
    pass

print("Top Level in one py")

if __name__ == '__main__':
    #RUN the script
    print('one.py is running directly')
    func1()
else:
    print('one.py has be imported')