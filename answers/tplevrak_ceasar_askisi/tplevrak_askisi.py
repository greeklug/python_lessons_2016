#!/usr/bin/python
# -*- coding: utf-8 -*-

import tplevrak_f_for_askisi

def main():
	
	gotananswer = 0
	choice='6'
	
	while gotananswer == 0:
	
		if choice == '1':
			tf_bruteforce()
			gotananswer=-1
		
		elif choice == '2':
			tf_cleverway()
			gotananswer=-1
		
		elif choice == '3':
			gotananswer=-1
			
		else:
			tf_drawMenu()
			choice=raw_input("     Enter your choice : ")
			print ''

	return 0

def tf_bruteforce():
	
	Originaldata = tplevrak_f_for_askisi.tf_main_encrypt_string('sd', 4, 'sd', 0)
	
	timestotry = len(Originaldata[0])
	counter = 0
	amiok = 0
	
	while amiok == 0:
		counter = counter + 1
		currenttest = tplevrak_f_for_askisi.tf_main_encrypt_string(Originaldata[3], counter, Originaldata[0], -1)
		print ''
		print '     Attempt No       : ' + str(counter)
		print '     Encrypted phrase : ' + Originaldata[3]
		print '     Current Result   : ' + currenttest[3]
		print ''
	
		if Originaldata[1] == currenttest[3]:
			amiok = -1
			print ''
			print '     Original phrase is -' + Originaldata[1] + '- and is found in ' + str(counter) + ' tries.'
			
		else:
			if counter > timestotry:
				amiok = -1
				print ''
				print '     I have tried solving this ' + str(counter) + ' times. It is more than enough. I quit'
			
def tf_cleverway():

	Originaldata = tplevrak_f_for_askisi.tf_main_encrypt_string('sd', 4, 'sd', 0)
	
	encryptstring = Originaldata[0]
	orgnlphrase = Originaldata[1]
	nmbrodshifts = Originaldata[2]
	rsltphrase = Originaldata[3]
	
	or1st = orgnlphrase[:1]
	rslt1st  = rsltphrase[:1]
	
	Orpos = encryptstring.find(or1st)
	Rspos = encryptstring.find(rslt1st)
	
	posdiff = abs(Rspos - Orpos)

	RecoveredPhrase = tplevrak_f_for_askisi.tf_main_encrypt_string(rsltphrase, (len(encryptstring) - posdiff), encryptstring, -1)

	tplevrak_f_for_askisi.tf_printresults(RecoveredPhrase, "      --- Detailed results of backwards encryption ---")
	

def tf_drawMenu():
	
	print ''
	
	for i in range(200):
		print ''
	
	print ''
	print '     ********************************************'
	print '     **                                        **'
	print '     **   Test Excercise for Python            **'
	print '     **                                        **'
	print '     **   Enter a phrase with latin letters    **'
	print '     **   and decimal numbers.                 **'
	print '     **                                        **'
	print '     **   It will be encrypted and then        **'
	print '     **   decrypted either with brute force    **'
	print '     **   or in a fast kind of way.            **'
	print '     **                                        **'
	print '     **   Please select if you want to try     **'
	print '     **   to decrypt with :                    **'
	print '     **                                        **'	
	print '     **   1 - The Brute Force Way              **'
	print '     **   2 - The Fast way                     **'
	print '     **   3 - Exit                             **'
	print '     **                                        **'
	print '     ********************************************'
	print ''

if __name__ == '__main__':
	main()

