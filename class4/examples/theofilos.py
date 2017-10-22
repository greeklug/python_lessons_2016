#!/usr/bin/python
# -*- coding: utf-8 -*-

# lista me frouta 5 sto synolo

tl_fr=['fr1','fr2','fr3','fr4','fr5']

tl_pr=[11,22,33,44,55]

def tf_calccost(l1,l2):
	
	td_01=dict(zip(l1,l2))
	
	#print td_01
	
	totalcost=0
	counter=0
	
	for x in td_01.itervalues():
		totalcost=totalcost+x
		counter=counter+1
		if counter >=3:
			
			break
	
	print totalcost
	
tf_calccost(tl_fr,tl_pr)
