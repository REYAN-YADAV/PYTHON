# Replacing string with another string.
 #syntax = string.replace('old','new') 
# ex1
s = "learning pytohn is difficult"
# replace difficult to easy
s1 = s.replace('difficult','easy')
print(s1)

# ex2
s = "learning pytohn is difficult"
# remove space
s1 = s.replace(' ','')
print(s1)

# write a program to find number of spaces present in the given string?

s = "learn python every day without thinking anything else"
slen = len(s)             # find length of string
s1 = s.replace(' ','')  # remove space
s1len = len(s1)  # length of s1 (string after removing space)
num_of_space = slen - s1len # number of space = length of s - length of s1
print(num_of_space)

# SPLITING OF STRING
# By using split method we can split any string.
# after split object type always we list
#ex 1=>
s = "learning python is very easy"
l = s.split(' ')
print(l)

#ex 2=>
s = "one, two, three"
l = s.split(',',1) # (,) - it is sepratare based on coma split the string and  1 represent maxsplit how many times you want to split
print(l)


# JOINING OF STRINGS:=>  A group of strings (list or tuple) can be joined by using the given delimeter
# syntax => seperator.join(group of string)

#ex 1.=>
l = ['sunn','bunn','chunn']
# combine with the help of - seperator
s = '-'.join(l)
print(s)

t = ['10','20','30']
# combine with no seprator
s = ''.join(t)
print(s)

# split = str to list
# join = (list/tuple) to str

















