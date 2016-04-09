# Εστω ότι έχουμε 1 λίστα και θέλουμε να κάνουμε ένα αντίγραφο αυτής
list1 = [1,2,3,4,5]

# μέθοδος πρώτη όπου κάνουμε αναφορά στην πρώτη λίστα
list2 = list1

# μετά από αυτό αν αλλάξουμε την list1 αλλάζει και η list2

list1.pop(0)
print "Λίστα1: {0}".format(list1)
print "Λίστα2: {0}".format(list2)

"""
prints
Λίστα1: [2, 3, 4, 5]
Λίστα2: [2, 3, 4, 5]
[Finished in 0.0s]
"""

# Αν θέλουμε το αντίγραφο της list1 να μην είναι reference σε αυτήν (να μην αλλάζει αν αλλάξουμε την πρώτη λίστα)
# τότε έχουμε διαφορετικούς τρόπους να το κάνουμε όπως παρακάτω
# μέθοδος slice
list1 = [1,2,3,4,5]
list2 = list1[:]

list1.pop(0)
print "Λίστα1: {0}".format(list1)
print "Λίστα2: {0}".format(list2)

"""
prints
Λίστα1: [2, 3, 4, 5]
Λίστα2: [1, 2, 3, 4, 5]
[Finished in 0.0s]
"""
# οπότε βλέπουμε ότι η list2 δεν άλλαξε ακόμα και αν αλλάξαμε την list1


# μέθοδος copy
import copy

list1 = [1,2,3,4,5]
list2 = copy.copy(list1)

list1.pop(0)
print "Λίστα1: {0}".format(list1)
print "Λίστα2: {0}".format(list2)

"""
prints 
Λίστα1: [2, 3, 4, 5]
Λίστα2: [1, 2, 3, 4, 5]
[Finished in 0.0s]
"""

# μέθοδος list comprehension
list1 = [1,2,3,4,5]
list2 = [x for x in list1]

list1.pop(0)
print "Λίστα1: {0}".format(list1)
print "Λίστα2: {0}".format(list2)

"""
prints 
Λίστα1: [2, 3, 4, 5]
Λίστα2: [1, 2, 3, 4, 5]
[Finished in 0.0s]
"""

# evaluating methods δηλαδή να δούμε τι είναι γρήγορο και τι όχι

import time

list1 = list(range(0,100000000))
time1 = time.time()
list2 = list1[:]
time2 = time.time()

print "Time passed for slice method: %s" %(str(time2-time1))

time1 = time.time()
list2 = list(list1)
time2 = time.time()

print "Time passed for list build method: %s" %(str(time2-time1))

time1 = time.time()
list2 = copy.copy(list1)
time2 = time.time()

print "Time passed with copy method: %s" %(str(time2-time1))

time1 = time.time()
list2 = [x for x in list1]
time2 = time.time()

print "Time passed with list comprehension method: %s" %(str(time2-time1))

"""
Time passed for slice method: 1.00920581818
Time passed for list build method: 1.62438106537
Time passed with copy method: 1.61925697327
Time passed with list comprehension method: 7.5519080162
"""

