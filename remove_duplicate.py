# write a program to remove duplicate character present in the given string?
                   # let input = 'AAAAAAAAABBBBBBBCCCCCCCDDDDDDDDDEEEEEEEE'
				   # expectedd output = ABCDE
s = input("Enter a string: ")
l = []
for x in s:
	if x not in l:
		l.append(x)
output = ''.join(l)
print(output)


# Write a program to find number of occurance is present in given string?
				# let input = ABCABCABBCDE
				# expected output = A-3,B-4,C-3,D-1,E-1

s = input("Enter a string: ")
d = {}      # empty dict
for x in s:
	if x not in d:  # the x key not in d
		d[x]=1
	else:
		d[x]=d[x]+1
print(d)  
for k,v in d.items():  # k=key v = values
	print(f'{k} occurs = {v} times')








