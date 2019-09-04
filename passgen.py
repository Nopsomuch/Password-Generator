#!/usr/bin/python3

import random
import pyperclip          								 #    Install pyperclip module

chars = "abcdefghijklmnopqrstuvwxyziABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890^?!?$%&/()=?`'+#*'~';:_,.-<>|"      # All characters | letters | numbers | special characters
passwd = ""


length = int(input("[-] Password Length: "))         					 #    Choose length of password
while len(passwd) != length:
	passwd = passwd + random.choice(chars)
	if len(passwd) == length:
		print("[+] Password: %s" % passwd)					 #    Prints password generated <-- comment out if you don't want it printed
		pyperclip.copy(passwd)							 #    Copies password to clipboard	
		print("[+] Password has been copied to clipboard!")
		print("")
