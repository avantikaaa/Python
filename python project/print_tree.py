import os
from dict_making import *
def printall(s, l):	#l is a dictionary
	for f in l:
		if( type(f) == dict ):
			for fil in f:
				print s +"|__ "+ fil
				fptr.write(s+"|__ "+str(fil)+"\n")
				printall(s+"| ", f[fil])
		else:
			print s+"|__ "+str(f)
			fptr.write(s+"|__ "+str(f)+"\n")



startpath = raw_input("Enter folder name: ")  #'Downloads/'#keep the dir name

#print dict_making(startpath)

fptr = open("DirectoryTree.txt", "w")
output = dict_making(startpath)
#main_list = [{'imt2019504': [{'code': ['student2.py', 'theory.org', 'student.py', 'institute.py', 'shapes.py', 'student1.py', 'mymath.py']}, 'a6.pdf']}, 'imt2019504.tar.gz', '8a5.py']
#for i in main_list: 			#change variable-> name of the main list
printall("", output)	#list
fptr.close()
print""
save = raw_input("Do you want to save this in a file?(y/n) ")
save = save.lower()
if (save == 'y'):
	print ""
	print "This is stored in the file \"DirectoryTree.txt\""
	print ""
else:
	os.system('rm DirectoryTree.txt')
