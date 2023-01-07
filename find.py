# finding substring
# There are four ways to find substring in the given string
# 1.find
# 2.index
# 3.rfind
# 4.rindex
# syntax = string.find(substring)
# syntax = string.find(substring,begin,end)
# syntax = string.index(substring)
# find method = it will return index of first occurrence of the given string
                # if return -1 then the given substring is not available
# rfind => rfind() will search complete string until finding last occurance in forward direction
# index method => it is exactly same as find method except that if the specified string not avialable then we will get value error 


#ex 1 =>
s= "learning python is very easy"  # here python occurrense is only one time so in both output we got same index
print(s.find("python"))  
print(s.rfind("python"))

#ex 2 =>
s= "learning python is very easy and python is fun" # here python occurrense are two time so in both output we got diffrence index
print(s.find("python"))
print(s.rfind("python"))



# write a program to find all occurance of the given substring?

s = input("Enter your string: ")
subs = input("Enter your substring which you want to find: ")
n=len(s)                                            # length of the input string
count=0                                               # occurance of substring
poss=0                                        # index of the first occurance of given substring
while True:
	i = s.find(subs,poss,n)
	if i == -1:                                # it represnt if sub string not found then will be execute this block
		break
	else:
		print("found at index", i)                  # i represent index of occuarances
		count = count+1
		poss = i+len(subs)                           # change the position from 0 to current occurances index + its length of string
print("The number of occurances of the given substring: ",count)   # total number of occurance

# method 2

# There is count() method function inbuilt in python
# syntax => string.count(substring,begin,end)
# or syntax => string.count(substring)

s = input("Enter your string: ")
subs = input("Enter your substring which you want to find: ")
occur = s.count(subs)
print(occur)























