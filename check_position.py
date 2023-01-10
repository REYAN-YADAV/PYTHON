# Find the caracter at even and odd position?
s = input("Enter any string: ")
even = []    # empty list for even position character
odd = []     # empty list for odd position character
i=0
while i<len(s):
	if i%2==0:              # check index i is even
		even.append(s[i])
	else:                    # index i is odd 
		odd.append(s[i])
	i=i+1
print(even)
print(odd)
e = ''.join(even)     # join string from list to str type
o = ''.join(odd)
print(o)
print(e)





