#a = 10
#b = 20
#c = 30 if a>b else 40
#print(c)


'''# write a python program to read int value from keyboard and print min value.
a = int(input("enter first number : "))
b = int(input("enter sec number : "))
min_value = a if a<b else b
print(min_value)'''

'''#write a python program to read int value from input and print min value.
a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))
min_value = a if a<b and a<c else b if b<c else c
print(min_value) '''

'''# write a python program to read value from input and print min value.
a = (input("enter first number : "))  
b = (input("enter sec number : "))        # this program compare with any int, float or string
min_value = a if a<b else b					# dought when compare with tuple
print(min_value) '''

'''#'#write a python program to read int value from input and print min value.
a = int(input("enter first number : "))
b = int(input("enter second number : "))   # in line 30. a<b<c it check number a is less b then less b less than c 
c = int(input("enter third number : "))
min_value = a if a<b<c else b if b<c else c
print(min_value)'''


'''# write a program read two int number from input let first and sec.
1. first= sec output should be first num and sec num are equal"
2 first> sec output should be first num is greater than sec number.
3 sec>first output should be sec num is greater than first num.

first_num = int(input("enter first number: "))
sec_num = int(input("enter sec num : "))
output = "first num and sec num are equal" if first_num == sec_num else "sec num is greater than first number" if first_num<sec_num else "first num is greater than sec number" 
print(output)'''











