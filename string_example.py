# write a program suppose every alphabet character followed by a single digit?
						# let input = a4b3c2
						# expected output = aaaabbbcc
#s = input("enter your string: ")
s = 'a4b3c2'
output = ''
for x in s:
	if x.isalpha():
		ch=x
	else:
		output = output + ch*int(x)
print(output)


#  write a program suppose every alphabet character followed by a some digit?
					# let input = 'a2b3c2'
					#expected output = aabbbcc
s = input("Enter the string: ")
output = ''
num = ''
i=0
while i<len(s):
	if s[i].isalpha():
		ch = s[i]
	else:
		num=num+s[i]
		if i==len(s)-1:
			output=output+ch*int(num)
		if i+1<len(s) and s[i+1].isalpha():
			output=output+ch*int(num)
			num=''
	i=i+1
print(output)



# write a program given string let input = 'a4k3b2' and expected output = 'aeknbd'
        # ord(a) = 97
		# chr(97) = a
s = 'a4k3b2'
output = ''
for x in s:
	if x.isalpha():
		ch=x
		output=output+ch
	else:
		output=output+chr(ord(ch) +int(x))
print(output)
	


















