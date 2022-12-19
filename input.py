'''x = input("Enter first number: ")
y = input("Enter second number: ")
i = int(x)
j = int(y)
print("The sum : ",i+j)


# you can write above code like this also
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("The sum : ",x+y)'''


#or
#print("The sum : " ,int(input("Enter first number: ")) + int(input("Enter sec number: ")))

'''#write a progam to read employee data from the keyword and print that data
eno = int(input("Enter employee No: "))
ename = input("Enter employee name: ")
esal = float(input("Enter employee salary: "))
eaddr = input("Enter employee address: ")
married = eval(input("Employee married? [True/False] : "))
print("Confirm Data")
print("employee Number: ",eno)
print("employee Name: ",ename)
print("employee salary: ",esal)
print("employee address: ",eaddr)
print("employee married : ",married)'''

'''# how to read input in single line.
s = input("enter 2 number :") #for space b/w two number use space bar when enter your number
print(s)
print(type(s))
l = s.split()
print(l)
print(type(l))
l1 = [int(x) for x in l]
print(l)
print(l1)
print(type(l1))
a,b = l1       # unpacking the list 
print(a)
print(b) 
print("the sum: ",a+b)'''

'''# above program in single line
a,b = [int(x) for x in input("Enter two seprated number: ").split()]
print("The sum: ",a+b)'''

'''# write a program to read 3 float values from keyword with comma sepration and print the sum in single line.
a,b,c = [float(x) for x in input("Enter number float value with , sepration: ").split(",")]
print("the sum of a,b and c: ",a+b+c)'''

'''x = eval(input("enter some thing: "))
print(type(x))'''

from sys import argv
#print(type(argv))
#input.py 10 20 30
print([0])





























