'''from sys import argv
print('the number of command line argment: ',len(argv))
print('the list of command line argment: ',argv)
print('the command line argment one by one: ')
for x in argv:
	print(x)'''

'''# write the program to print the sum of given number provided as cmd line argument.
from sys import argv
a = argv[1:]
sum = 0
for x in a:
	sum = sum + int(x)
print("The sum : ",sum) '''

from sys import argv
print(argv[100])
#py test.py sunny leone
  #=> sunny
#py test.py "sunny leone"
 #=> sunny leone '''


'''from sys import argv
#print(argv[1] + argv[2]) #(1)
#py test.py 10 20
# => 1020            #bcos here 1 consider as str type in str type + means concatanation.

print(int(argv[1]) + int(argv[2]))
# py test.py 10 20
# => 30'''