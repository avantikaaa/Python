#!/usr/bin/env python
import os
from dict_making import *
def printall(s, l):	#l is a dictionary
	for f in l:
		if( type(f) == dict ):
			for fil in f:
				print s +"`->"+ fil
				fptr.write(s+"`->"+str(fil)+"\n")
				printall(s+"|  ", f[fil])
		else:
			print s+"`->"+str(f)
			fptr.write(s+"`->"+str(f)+"\n") 	
"""			
address = raw_input("Enter address of the directory from home: ")
if(address = "\n"):
	continue
else:
	os.chdir(address)"""
startpath = raw_input("enter directory name: ")
fptr = open(str(startpath)+".txt", "w")
output = dict_making(startpath)	

"""
command = " .."
os.system(command)
path = raw_input("Enter folder address: ")  #'Downloads/'#keep the dir name
command = "cd " + path
os.system(command)
os.system("cd sample")
os.system("ls")
startpath = raw_input("Enter folder name: ")
#print dict_making(startpath)
#x = raw_input("")
fptr = open(str(startpath)+".txt", "w")
output = dict_making(startpath)
#main_list = [{'imt2019504': [{'code': ['student2.py', 'theory.org', 'student.py', 'institute.py', 'shapes.py', 'student1.py', 'mymath.py']}, 'a6.pdf']}, 'imt2019504.tar.gz', '8a5.py']
#for i in main_list: 			#change variable-> name of the main list


"""
printall("", output)	#list
fptr.close()
print""
save = raw_input("Do you want to save this in a file?(y/n): ")
save = save.lower()
if (save == 'y'):
	print ""
	print ("This is stored in the file " +startpath +".txt")
	print ""
else:
        s=startpath+".txt"
        cmd = "rm " + s
	os.system(cmd)
