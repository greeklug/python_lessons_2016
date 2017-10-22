#!/usr/bin/python
# -*- coding: utf-8 -*-

def addTwoNumbers(x,y = 0):
	"""
	Adds two numbers provided as keyword arguments
	params:
		x: the first integer as regular argument and is required
		y: the second integer as keyword argument
		   defaults to 0 (zero)
	return:
		result: integer resulted by adding the two numbers
	"""
	result = x + y
	return result

if __name__ == '__main__':
    x = addTwoNumbers(1,2)
    print x
