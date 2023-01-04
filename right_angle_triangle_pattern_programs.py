'''# To print right angle triangle pattern with * symbol
# let n=3, output = *
#					* *
#					* * *
      
n = int(input("Enter number of rows: "))
for i in range(n):
	for j in range(i+1):
		print('* ',end=' ')
	print()




# To print right angle triangle pattern with with fixed digit in every row?
# let n=3, output = 1
#					2 2
#					3 3 3

n = int(input("Enter number of rows: "))
for i in range(n):
	print((str(i+1)+' ')*(i+1))


# write a program to print right angle triangle pattern ?
# let n=3, output = 1
#					1 2
#					1 2 3

n = int(input("Enter number of rows: "))
for i in range(n):
	for j in range(i+1):
		print(j+1,end=' ')
	print()

'''
# write a program to print right angle triangle pattern ?
# let n=3, output = A      ASCII value for A = 65
#					B B
#					C C C


n = int(input("Enter number of rows: "))
for i in range(n):
	print((chr(65+i)+' ')*(i+1))









'''

# write a program to print right angle triangle pattern ?
# let n=3, output = A
#					A B
#					A B C

n = int(input("Enter number of rows: "))
for i in range(n):
	for j in range(i+1):
		print(chr(65+j),end=' ')
	print()

'''








