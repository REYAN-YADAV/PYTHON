# Write a program to sort character present in the given string? first alphabet the nnumber value?
			# let input = 'B4A1D3'
			# expected output = 'BAD413'

s = input("Enter your string: ")
s1 = ''
s2 = ''
output = ''
for x in s:
	if x.isalpha():  # every alphabet character store in s1
		s1=s1+x
	else:
		s2=s2+x   # every digit characer store in s2
print(s1)
print(s2)
for x in sorted(s1):
	output=output+x
for x in sorted(s2):
	output=output+x
print(output)




