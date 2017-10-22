#!/usr/bin/python
# -*- coding: utf-8 -*-

# lista me frouta 5 sto synolo

frouta = ['karpouzi','milo','axladi','portokali','mantarini','banana']
times = [1,2,3,4,5]

def sumTimes(l1, l2):
	a = [l1[i] for i in range(3)]
	b = [l2[i] for i in range(3)]
	return sum(dict(zip(a, b)).values())
	
print sumTimes(frouta, times)
