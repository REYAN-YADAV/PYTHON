# Write a program to read string from the keyword and display its character by index wise both positive and negative

# positive index wise
s = input("enter any string: ")
i= 0   
#here i consider for loop bcoz if i need all character in the given string without any condition.
for x in s: 
	print(f'index {i} = chr {x}') # where i represent index and x represent character of the string
	i=i+1

#or using while loop
s = input("enter any string: ")
i=0  
while i<len(s):
	print(f'index = {i} , chr = {s[i]}')
	i=i+1


#negative index wise
s = input("enter any string: ")
i=-len(s)     # it represent negative index
for x in s:
	print(f'index {i} = chr {x}')
	i = i+1

# or
s = input()
i=0
for x in s:
	print(f'index {i-len(s)} = chr {x}')
	i=i+1


# negative index by while loop

s = input("enter any string: ")
i=-1
while i>=-len(s):
	print(f'index {i}, chr {s[i]}')
	i=i-1

#or
s = input("enter any string: ")
i=-len(s)
while i<=0:
	print(f'index {i}, chr {s[i]}')
	i=i+1















