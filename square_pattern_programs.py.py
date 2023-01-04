# To print given number of *s in a row?
n = int(input("Enter number of rows: "))
for i in range(n):
	print('*',end=' ')


# To print square pattern with *s symbol?
n = int(input("Enter number of rows: "))
for i in range(n):
	print('* '*n)


#To print square pattern with provided fixed digit ?
n = int(input("Enter number of rows: "))   # let 1row = 1unit , n = n unit lenght and breadth 
d = int(input("Enter the digit which you want to ptint: "))
for i in range(n):
	print((str(d)+ ' ')*n)


# To print square pattern provided fixed digit in every row?
n = int(input("Enter number of rows: "))
for i in range(n):
	print((str(i+1)+ ' ')*n) 



# To print square pattern provided  alphabet symbol in every row?
n = int(input("Enter number of rows: "))
for i in range(n):
	print((chr(65+i)+' ')*n)


#To print square pattern with digit?   
# let n=3, output = 1 2 3 
#					1 2 3
#					1 2 3
n = int(input("Enter number of rows: "))
for i in range(n): 
	for j in range(n):  # represent column
		print(j+1,end=' ')
	print()

#To print square pattern with alphabet symol in dictonary order?
# let n=3, output = A B C 
#					A B C 
#					A B C 

n = int(input("Enter number of rows: "))
for i in range(n): 
	for j in range(n):  # represent column
		print(chr(65+j),end=' ')
	print()

#To print square pattern with fixed digit in desending order?
# let n=3, output = 3 3 3 
#					2 2 2 
#					1 1 1

n = int(input("Enter number of rows: "))
for i in range(n): 
	print((str(n-i)+' ')*n)

#To print square pattern with alphabet symol in dictonary order?
# let n=3, output = C C C   => for i=0 ,c=67(ASCII value of letter C) = 65+n-i-1 = 64+n-i  
#					B B B 
#					A A A

n = int(input("Enter number of rows: "))
for i in range(n): 
	print((chr(64+n-i)+' ')*n)


#To print square pattern with  digit in desending order?
# let n=3, output = 3 2 1
#					3 2 1
#					3 2 1

n = int(input("Enter number of rows: "))
for i in range(n): 
	for j in range(n):  # represent column
		print(n-j,end=' ')
	print()


#To print square pattern with alphabet symbol in dictonary order?
# let n=3, output = C B A   => for J=0 ,c=67(ASCII value of letter C) = 65+n-i-1 = 64+n-i  
#					C B A 
#					C B A

n = int(input("Enter number of rows: "))
for i in range(n): 
	for j in range(n):  # represent column
		print(chr(64+n-j),end=' ')
	print()
































