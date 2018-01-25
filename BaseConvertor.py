#!/usr/bin/python

# input
num = 2018

# base 
base = 9

# collect
out = []

# result
result = ""

while num > base:
	# result
	tmp = num/base
	#print "result =>", result

	# rem
	rem = num - (tmp * base)
	#print "rem =>", rem
	out.append(rem)

	num = tmp

	if num < base:
		out.append(num)

for i in reversed(out):
	result += str(i)

print result
