# CHANGING CAASE OF A STRING
#*****************************
# 1.upper() = Every lower case character will be converted into uppercase
# 2.lower() = Every upper case character will be converted into uppercase
# 3.swapcase() = lower to upper and upper to lower
# 4.title() = Every first character of word will be uppercase in a sentence
#5.capitalize() = first character in upper case in sentence

#EX=>
s = "learning python is very 95 easy"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())

# TO CHECK TYPE OF CHARACTER PRESENT IN THE GIVEN STRING
#1.isalnum() = Returns True if all characters in the string are alphanumeric (i.e a to z, A to Z, 0 to 9 )
#2.isalpha() = Returns True if all characters in the string are in the alphabet (a to z, A to Z)
#3.isdigit() = Returns True if all characters in the string are digits (0 to 9)
#islower() = Returns True if all characters in the string are lower case
#isupper() = Returns True if all characters in the string are upper case
#istitle() = Returns True if the string follows the rules of a title
#isspace() = if string contain only space

# write a program to check type of character of given string?
s = input("Enter any string: ")
if s.isalnum():
	print("This string is alphanumeric ",end="and ")
	if s.isalpha():
		print("This string is alpha ",end="and ")
		if s.islower():
			print("this string is lower")
		else:
			print("this string is upper")
	elif s.isdigit():
		print("this string is digit")
	else:
		print(" nothing")

elif s.isspace():
	print("This string contain only space")
else:
	print("non space special character")

# Checking starting and ending part of the string?
s = "learning python is very easy"
print(s.startswith('l'))
print(s.startswith('p'))
print(s.startswith('easy'))
print(s.startswith('learning'))
print(s.endswith('l'))
print(s.endswith('y'))
print(s.endswith('e'))
print(s.endswith('easy'))





	
