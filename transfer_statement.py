  # TRANSFER STATEMENT .


#Example 1. use break transfer statement

for i in range(10):
	if i==7:
		print("processing is enough")
		break
	print(i)
print("outside of loop")   



#Example 2. wrt program based on this cart [10,20,30,600,70,80] if item is greater than 500. 
           #     print insurence is required and break the iteration.

cart = [10,20,30,600,70,80]
for item in cart:
	if item>500:
		print("To place this order, insurence must be required")
		break
	print("The processing item: ",item)   


#Example 3.

x=40
if x>40:
	print("We are stopping program")
	break
print("hello")     # if you run this code you get syntax error Because without loop you cannot use break statement  



#Example 4. program on continue statement. print odd number from 0 to 10.

for i in range(10):
	if i%2==0:
		continue
	print(i)   


#Example 5. wrt program based on this cart [10,20,30,600,700,80,90] if item is greater than 500.
       #           print insurence is required and continue.


cart = [10,20,30,600,700,80,90]
for item in cart:
	if item>500:
		print("Insurence is required: ",item)
		continue
	print("processing Item: ",item)  



#Example 6. wrt program list [10,20,0,5,0,30] divide each element of list by 100 and printout.

list = [10,20,0,5,0,30] 
for x in list:
	if x==0:
		print("Hello stupid, How we can divide with zero")
		continue
	print("100/{} = {}".format(x,100/x)) 



#Example 7.

x=40
if x>40:
	print("We are continue program")
	continue
print("hello")     # if you run this code you get syntax error Because without loop you cannot use continue statement 






#   NESTED LOOP FOR BREAK AND CONTINUE.

# Example 8.

for i in range(6):
	for j in range(4):
		if i==j:
			break          # In nested loop break statement apply for inner loop
		print(i,j)


# Example 9

k=0
for i in range(6):
	for j in range(4):
		if i==j:
			continue
		k=k+1               # In nested loop continue statement apply for inner loop
		print(i,j)          # (3)
print(k)                    # it give total number of equation (3) executed.



#  *LOOP WITH ELSE BLOCK*

#EXAMPLE 10.  Loop with else block with break statement.

cart = [10,20,30,40,50]
for item in cart:
	if item>500:
		print("we cant process this item")
		break                                   # loop without break then only else block executed.
	print("processing item: ",item)              # if in executing break block execute then else block will not be execute.
else:
	print("congratulation all items processed successfuly")



#EXAMPLE 11.  Loop with else block with continue statement.

cart = [10,20,30,600,40,50]
for item in cart:
	if item>500:
		print("we cant process this item")
		continue                                   # loop with else block with continue  else block always  execute.
	print("processing item: ",item)
else:
	print("congratulation all items processed successfuly")



#  *PASS STATEMENT*

#EXAMPLE 1.

def f1():
	pass

#EXAMPLE 2.

x = int(input("Enter marks: "))
if x>40:
	print("you passed exam")
else:
	pass       # else block always expecting some implmentation but if you not confirm what you want to
	                  #  emplement then use pass satement it is place holder for future implementation.


#  del Statement

#Example 1. 
x=10
print(x)
del(x)
print(x)     # it show name error bcoz x variable is delete


#Example 2. 

s1 = 'reyan'
s2 = s1
s3 = s2       # here object 'reyan' does not eligibl for garbage collection. bcoz multiple refrences are there if you 
del(s1)           #  delete all refrences then the object is eligible for garbage collection.
print(s2)
print(s3)



# Example 3. del vs immutable objects.

s = 'reyan'
del(s[0])     #TypeError: 'str' object doesn't support item deletion bcoz str object are immutable in nature.

#Example 4. del vs none

x=10
x=None
print(x)








































































	
