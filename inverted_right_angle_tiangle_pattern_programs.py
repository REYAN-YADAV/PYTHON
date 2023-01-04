# Write a program to print inverted right angle triangle pattern with * symbol?
# let n=3, output = * * *
#					* *
#					*


n = int(input("Enter right angle triangle: "))
for i in range(n):
	print('* '*(n-i))



# Write a program to print inverted right angle triangle pattern?
# let n=4, output = 1 1 1 1
#					2 2 2
#					3 3
#					4

n = int(input("Enter right angle triangle: "))
for i in range(n):
	print((str(i+1)+' ')*(n-i))




# Write a program to print inverted right angle triangle pattern?
# let n=4, output = A A A A
#					B B B
#					C C
#					D

n = int(input("Enter right angle triangle: "))
for i in range(n):
	print((chr(65+i)+' ')*(n-i))




# Write a program to print inverted right angle triangle pattern?
# let n=4, output = 4 4 4 4
#					3 3 3
#					2 2
#					1

n = int(input("Enter right angle triangle: "))
for i in range(n):
	print((str(n-i)+' ')*(n-i))






# Write a program to print inverted right angle triangle pattern?
# let n=4, output = D D D D here D = 68 = 65+n-1-i 
#					C C C
#					B B
#					A

n = int(input("Enter right angle triangle: "))
for i in range(n):
	print((chr(64+n-i)+' ')*(n-i))





# Write a program to print inverted right angle triangle pattern?
# let n=4, output = 1 2 3 4
#					1 2 3
#					1 2
#					1

n = int(input("Enter right angle triangle: "))
for i in range(n):
	for j in range(n-i):
		print(j+1,end=' ')
	print()




# Write a program to print inverted right angle triangle pattern?
# let n=4, output = A B C D
#					A B C
#					A B
#					A

n = int(input("Enter right angle triangle: "))
for i in range(n):
	for j in range(n-i):
		print(chr(65+j),end=' ')
	print()



# Write a program to print inverted right angle triangle pattern?
# let n=4, output = 4 3 2 1
#					3 2 1
#					2 1
#					1

n = int(input("Enter right angle triangle: "))
for i in range(n):
	for j in range(n-i):
		print(n-j,end=' ')
	print()



# Write a program to print inverted right angle triangle pattern?
# let n=4, output = D C B A
#					C B A
#					B A
#					A

n = int(input("Enter right angle triangle: "))
for i in range(n):
	for j in range(n-i):
		print(chr(64+n-j),end=' ')
	print()




























