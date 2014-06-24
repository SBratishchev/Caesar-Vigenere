#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import sys

def Caesar(text, key, flag):
    code = ''
    for c in text:
	if flag:
            code += chr((ord(c) + key) % 128)
	else:
	    code += chr((ord(c) - key) % 128)
            
    return code


def Vigenere(text, key, flag):
    iter = 0
    code = ''
    for c in text:
	    if flag:
                code += chr((ord(c) + ord(key[iter])) % 128)
            else:
                code += chr((ord(c) - ord(key[iter])) % 128)
	    iter = (iter + 1) % len(key)             
    return code

  

def alert():  
	if len(sys.argv) != 6:
		print "command <input_file> <output_file> <key> <c(Caesar) or v(Vigenere)> <c(crypt) or d(decrypt)>";
		sys.exit();


alert()

f1 = open(sys.argv[1],"r");
text = f1.read();
f1.close;
f2 = open(str(sys.argv[2]), 'w')


if sys.argv[4] == "c":
	if sys.argv[5] == "c":
		f2.write(Caesar(text, int(sys.argv[3]), 1))
	elif sys.argv[5] == "d":
		f2.write(Caesar(text, int(sys.argv[3]), 0))
	else:
		alert()
elif sys.argv[4] == "v":
	if sys.argv[5] == "c":
		f2.write(Vigenere(text, str(sys.argv[3]), 1))
	elif sys.argv[5] == "d":
		f2.write(Vigenere(text, str(sys.argv[3]), 0))
	else:
		alert()
else:
	alert()

