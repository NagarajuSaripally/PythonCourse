'''
Pig Latin: Rules

if word starts with a vowel, add 'ay' to end
if word does not start with a vowel, put first letter at the end, then add 'ay'
word -> ordway
apple -> appleay
'''


def pig_latin(word):
	initial_letter = word[0]

	if initial_letter in 'aeiou':
		translated_word = word + 'ay'
	else:
		translated_word =  word[1:] + initial_letter + 'ay'

	return translated_word

print(pig_latin('word'))
print(pig_latin('apple'))