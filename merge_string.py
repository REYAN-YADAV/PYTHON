# write a program to merge character of 2 string into single string by taking character alternatively?
              # let input1 = rey
               # let input2 = yadav
			   # expected output = ryeaydav

s1 = input("Enter 1st string: ")
s2 = input("Enter 2st string: ")
i,j=0,0
output=''
while i<len(s1) or j<len(s2): # atleast one string contain character
	if i<len(s1):
		output = output + s1[i]
		i=i+1
	if j<len(s2):
		output = output + s2[j]
		j=j+1
print(output)

