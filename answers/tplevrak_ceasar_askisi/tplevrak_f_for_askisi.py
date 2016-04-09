#!/usr/bin/python
# -*- coding: utf-8 -*-



def shift_list(x,lista):

	lista5 = [y for y in lista]
	
	for i in range(x):
		last_char=lista5.pop(-1)
		lista5.insert(0,last_char)

	return lista5


def create_lookup(lista):
	
	dictlookup = {}
	
	for i in range (0, len(lista)):
		dictlookup[i] = lista[i]

	return dictlookup

def create_encryptkey(listx,listy):			
	
	key= {}
	key = dict(zip(listx,listy))

	return key

def encrypt_sentence(sentence,letters_in_list,shifted):
	
	newsentence=''
	
	lookup_dict = create_encryptkey(letters_in_list, shifted)
	
	for char in sentence:
		new_char = lookup_dict[char]
		newsentence = newsentence + new_char

	return newsentence

def tf_main_encrypt_string(sentence='test sentence', placestomove=4, enstring='abcdefghijklmnopqrstuvwxyz ', keepsilent=0):
	
	if keepsilent==-1:
		5==5
	else:
		print ''
		print ''
		
		sentence=raw_input("     Enter Phrase to Code : ")
		placestomove=raw_input("     Enter Shift Number   : ")
		placestomove=int(placestomove,10)
		
		enstring='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890'
		
	
	lettersinlist=list(enstring)	
	shifted = shift_list(placestomove,lettersinlist)
	
	resultphrase=''
	
	resultphrase = encrypt_sentence(sentence,lettersinlist,shifted)

	encryptreturn=[enstring , sentence, placestomove, resultphrase]
	
	if keepsilent==-1:
		5==5
	else:	
		print '     Resulting Phrase     : -' + resultphrase + '-'
		print ''	
		
		tf_printresults(encryptreturn, "      --- Detailed results of forward encryption ---")
		#print encryptreturn
	
	return encryptreturn
	
def tf_printresults(returnlist, resultstitle = '      --- Detailed Results --- '):
		print ''
		print ''
		print ''
		print resultstitle
		print ''
		print '     Encryption string    : -' + returnlist[0] + '-'
		print '     Original Sentence    : -' + returnlist[1] + '-'
		print '     Number of shifts     : -' + str(returnlist[2]) + '-'
		print '     Result sentence      : -' + returnlist[3] + '-'
		print ''	

if __name__ == "__main__":
	
	tf_main_encrypt_string('sd',1,'sd',0)
