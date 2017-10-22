#!/usr/bin/python
# -*- coding: utf-8
import time
#Δείκτης άμεσης εκτέλεσης αρχείου
print __name__
globaltime = 0


#Δήλωση γενικής function προσθήκης δύο αριθμών
#με προκαθορισμένα ορίσματα δύο μεταβλητές a και b
#οι οποίες έχουν προκαθορισμένες τιμές 2 και 4
def addTwoNumbers():
	"""
	Adds 2 predifiend numbers and prints the result
	params:
			a: 2
			b: 4
	"""
	a = 2
	b = 4
	c = a + b
	print c


print "##################"
print "ΕΦΑΡΜΟΓΗ ΑΘΡΟΙΣΜΑΤΟΣ ΔΥΟ ΠΡΟΚΑΘΟΡΙΣΜΕΝΩΝ ΑΡΙΘΜΩΝ"
print "##################"
print "Αποτέλεσμα:"
addTwoNumbers()
print "##################"
print "\n"


#Δήλωση γενικής function προσθήκης δύο αριθμών
#με προκαθορισμένα ορίσματα δύο μεταβλητές a και b
#οι οποίες σε περίπτωση κενής εισαγωγής είναι μηδέν
def addTwoNumbersVar(a=0,b=0):
	"""
	Adds 2 numbers and prints the result
	params:
			a: integer not required
			b: interger not required
	Ιf the input values are empty, 0 is implied
	"""
	time1 = time.time()
	c = a + b
	time2 = time.time()
	timediff = time2 - time1
	return timediff, c

timelapsed, result = addTwoNumbersVar(2,10)
print "##################"
print "ΕΦΑΡΜΟΓΗ ΑΘΡΟΙΣΜΑΤΟΣ ΔΥΟ ΜΕΤΑΒΛΗΤΩΝ ΑΡΙΘΜΩΝ"
print "2 + 10"
print "##################"
print "Αποτέλεσμα:"
print result
print "----------------"
print "Xρόνος που πέρασε:"
print timelapsed
print "##################"
print "\n"


print "##################"
print "ΕΚΠΤΥΠΩΣΗ ΑΘΡΟΙΣΜΑΤΟΣ ΔΥΟ ΜΕΤΑΒΛΗΤΩΝ ΑΡΙΘΜΩΝ"
print "11 + 9, ΕΦΟΣΟΝ ΤΟ ΑΡΧΕΙΟ ΕΚΤΕΛΕΙΤΑΙ ΑΜΕΣΑ"
print "##################"
if __name__ == '__main__':
	timelapsed, result = addTwoNumbersVar(11,9)
	print "Αποτέλεσμα:"
	print result
	print "----------------"
	print "Xρόνος που πέρασε:"
	print timelapsed
	print "##################"
print "\n"

