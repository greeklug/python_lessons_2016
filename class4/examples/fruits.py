#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fruits.py
#  
#  Copyright 2016 Greeklug Team <greeklug.gr>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#Λίστα φρούτων
l_fr = ['banana', 'axladi', 'milo', 'karpouzi', 'peponi']
#Λίστα τιμών
l_pr = [1.00, 1.25, 2.10, 5.00, 3.45]

def friutCost(l1,l2,c): 

    l3=dict(zip(l1, l2))
    #print l3
    
    counter = 0
    totalcost = 0
    
    for fruitcost in l3.itervalues():
		#print fruitcost
		totalcost = totalcost + fruitcost
		counter = counter + 1
		if counter >=c:
			print "##################"
			print "ΕΦΑΡΜΟΓΗ ΑΘΡΟΙΣΜΑΤΟΣ ΤΙΜΩΝ ΦΡΟΥΤΩΝ"
			print "##################"
			print "Φρούτα που προστέθηκαν:"
			print c
			print "----------------"
			print "Αποτέλεσμα σε Ευρώ:"
			print totalcost
			print "##################"
			print "\n"
			break

friutCost(l_fr,l_pr,3)
