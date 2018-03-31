"""
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
"""
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False


"""
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.


monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
"""

def monkey_trouble(a_smile, b_smile):
  if (a_smile and b_smile) or (not a_smile and not b_smile):
    return True
  else:
    return False


"""

Given two int values, return their sum. Unless the two values are the same, then return double their sum.


sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8

"""

def sum_double(a, b):
  if a == b:
    return (a + b) * 2
  else:
    return a + b

"""
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.


diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
"""

def diff21(n):
  subtractedValue = abs(n - 21)
  if n > 21:
    return 2 * subtractedValue
  return subtractedValue


"""
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
"""
def parrot_trouble(talking, hour):
  if talking and ( hour < 7 or hour > 20):
    return True
  else:
    return False

"""
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True

"""

def makes10(a, b):
  if a == 10 or b == 10 or a + b == 10:
    return True
  else:
    return False

"""
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.


near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
"""

def near_hundred(n):
  if n in range(90, 111) or n in range(190, 211):
    return True
  else:
    return False

"""

Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.


pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
"""
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return (a < 0 and b > 0) or (a > 0 and b < 0)


"""

Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.


not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""

def not_string(str):
  if len(str) >= 3 and str[0] == 'n' and str[1] == 'o' and str[2] == 't':
    return str
  else:
    return 'not ' + str


"""

Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
"""

def missing_char(str, n):
  myString = ''
  for index, character in enumerate(str):
    if index != n:
      myString += character
  return myString

"""

Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""

def front_back(str):
  if len(str) <= 1:
    return str
  else:
    first = str[-1]
    last = str[0]
    return first + str[1:len(str)-1] + last

"""
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.


front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
"""

def front3(str):
  if len(str) < 3:
    return '' + (str * 3)
  else:
    return '' + (str[:3] * 3)

"""
Given a string and a non-negative int n, return a larger string that is n copies of the original string.


string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""

def string_times(str, n):
  return ''+ str * n


"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;


front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
"""

def front_times(str, n):
  if len(str) >= 3:
    myString = str[0:3]
    return '' + myString * n
  else:
    return '' + str * n


"""
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""

def string_bits(str):
  return str[::2]


"""
Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""

def string_splosion(str):
  count = 0
  resultString = ""
  while count < len(str):
    for index, character in enumerate(str):
      if(count >= index):
        resultString += character
    count += 1
  
  return resultString

"""

Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
"""

def last2(str):
  # Screen out too-short string case.
  if len(str) < 2:
    return 0
  
  # last 2 chars, can be written as str[-2:]
  last2 = str[len(str)-2:]
  count = 0
  
  # Check each substring length 2 starting at i
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count

"""

Given an array of ints, return the number of 9's in the array.


array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
"""
def array_count9(nums):
  count = 0
  for num in nums:
    if num == 9:
      count += 1
  return count

"""

Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.


array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
"""

def array_front9(nums):
	return (9 in nums[0:4])


"""
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
"""

def array123(nums):
    if len(nums) >= 3:
        for ind, lst in enumerate(nums):
            if(ind+2) <= len(nums)-1:
                if nums[ind] == 1 and nums[ind+1] == 2 and nums[ind+2] ==3:
                    return True
    return False


"""

Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
"""

def string_match(a, b):
  count = 0
  for ind, character in enumerate(a):
    for i, char in enumerate(b):
      if (a[ind:ind+2] == b[i:i+2]) and (len(a[ind:ind+2]) > 1) and (len(b[i:i+2])>1) and (ind == i):
        count += 1
  return count