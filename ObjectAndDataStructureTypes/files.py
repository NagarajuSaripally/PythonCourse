'''
Simple I/O files
'''

my_file = open('myfile.txt');

print('read() method returns the whole text in the file as a string {}'.format(my_file.read())) 


'''
Every time when we read a text file we need to reset the cursor to starting point of a file to
read it again.
In order to achieve that Python has a built in function called `seek()`

please find it below with an exmaple
'''

my_file.seek(0) # here 0 means index with start beginning of the file

# now do the read again
print('read() method returns the whole text in the file as a string {}'.format(my_file.read()))


'''
Instead of printing everything in a gaint string, we can print each line in the text file as a separate string
using `readlines()` method

Check the following example, before printing reseting back to 0
'''

my_file.seek(0)

print('readlines() method returns the whole text in the file as a string {}'.format(my_file.readlines()))

'''
 We need to close the files for best practices after we done working with the files to avoid complicated errors later on
'''

my_file.close();


'''
 To avoid manually closing the files, we can use another approach to open up the file
'''


with open('myfile.txt') as my_new_file:
	contents = my_new_file.readlines()


print("Another way of opening the file using with: {}".format(contents))


'''
We can also write and overrite the files:
'''

# write to the file
# mode W means only able to overwrite to file
# default is r which mean readonly
# mode a means only append the text to file
# mode r+ is doing for reading and writing
# mode w+ is doing for writing and reading

#append text 
with open('myfile.txt', mode='a') as f:
	f.write("\nFouth on fouth")

with open('myfile.txt', mode='r') as f:
	printing = f.readlines()


print("Appedning text to file: {}".format(printing))


# overwrite existing file or creates a new file if there is a no file

with open('myfile.txt', mode='w') as f:
	f.write("\I created this text")

with open('myfile.txt', mode='r') as f:
	printing = f.readlines()


print("Appedning text to file: {}".format(printing))
