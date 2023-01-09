# Write a program to reverse the given string?
s = input("Enter any string: ")
print(s[::-1])

# method 2
s = input("Enter any string: ")
r = reversed(s) # the reversed function will reverse every character of string from index 0 to len(s) --> len(s) to 0
print(type(r))   # type of reversed funtion is reversed type
l = ''.join(r) # it will join all character into string
print(l)

# method 3
s = input("Enter any string: ")
l = ''
x = len(s)-1
while x>=0:
	l = l+s[x]
	x=x-1
r = ''.join(l)
print(r)



# Write a program to reverse internal content of each word?
# method 1
s = input("Enter any string: ") # let input = "one two three"
out = []                      # requarement = "eno owt eerht"
r = s.split()
for i in r:
	#print(i)
	k = reversed(i)
	res = ''.join(k)
	out.append(k)
	rev = ' '.join(out)
print(rev)

# method 2
s = input("Enter any string: ") # let input = "one two three"
out = []                      # requarement = "eno owt eerht"
i = 0
r = s.split()
while i<len(r):
	l = reversed(r[i])
	k = ''.join(l)
	out.append(k)
	output = ' '.join(out)
	i=i+1
print(output)

# method 3
s = input("Enter any string: ")
l = s.split()
l1 = []
for x in l:
	l1.append(x[::-1])
out = ' '.join(l1)
print(out)
 



# write a program to reverse order of words?
       # let input = "Learing python is very easy"
	   # expected output = "Easy very is python learning"

s = input("Enter any string: ")
l = s.split()
l1 =[]
i = len(l)-1
while i>=0:
	l1.append(l[i])
	i=i-1
out = ' '.join(l1)
print(out)



# Write a program to reverse every sec word in a string?
	# let input = "one two three four"
	# expected output = "one owt three ruof"
s = input("Enter any string: ")
l = s.split()  #The split() method splits a string into a list.You can specify the separator, default separator is any whitespace.
l1 = []        # it will create an empty list
i=0
while i<len(l):
	if i%2!=0:    # if index is odd reversed the element of that index and append to the l1 
		r = reversed(l[i])   
		j = ''.join(r)   # it will convert reversed type into str
		l1.append(j)
	else:                 # else index is not odd just append the element of that index
		l1.append(l[i])
	i=i+1
print(l1)
output = ' '.join(l1)
print(output)

