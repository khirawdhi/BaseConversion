#!/usr/bin/python

import sys

def main():
	num = int(sys.argv[1])
	base = int(sys.argv[2])

	#print num, base
	out = []

	result = ""

	while num > base:
		
		tmp = num/base
		
		rem = num - (tmp * base)
		
		out.append(rem)

		num = tmp

		if num < base:
			out.append(num)

	for i in reversed(out):
		result += str(i)

	print result


if __name__== "__main__":
	main()