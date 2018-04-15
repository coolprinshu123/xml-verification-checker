import sys                                       #importing various packages.
import re
param = sys.argv[1]                              #Getting the first argument in the string.
list1 = []                                       #List for containing the tags name.
list2 = []
flag = 0                                         #whenever any case is violated then the flag is changed.
with open(param,"r") as file:                    #opening the input file.
	for line in file:                        #Reading the file line by line.
		exp = re.compile('<+\w+')        #Regular expression for checking the opening tag.
		exp2 = re.compile('<+\/+\w+')    #Regular expression for closing tag.
		#exp3 = re.compile('\w+')
		for r in exp.findall(line):      #Finding all the opening tag in the file.
			#print r
			x = r[1:]                #Extracting the tag name.
			#print x
			list1.append(x)          #putting the name in the list.
			list2.append(x)
			if x.isalpha() == False: #If the tag name contains other  than characters.
				#print "Has Numbers"
				flag = 1         #Flag is 1.
		for t in exp2.findall(line):     #Finding all the closing tags in the line.
			#print t
			x = t[2:]                #Extracting the closing tag name.
			#print x
			list1.append(x)          #Putting the name in the list.
			if len(list2) > 0:       #If the list is not empty
				if list2[-1] == x:  #If the top element has the same name as closing tag.
					list2.pop() #Removing the top element.
				else:               #Else it is not balanced.
					#print "Not balanced"
					flag = 1
			else :                      #If the list is empty.
				flag = 1
			if x.isalpha() == False:    #If the tag name contains other than characters.
				#print "Has Numbers"
				flag = 1
if(list1[0] != list1[-1]):                          #Checking whether the first and last name is same or not.
	flag = 1
	#print "Not same"
 
if(flag == 1):                                      #If any error is found then print not well formed.
	print "Not Well formed"
else :                                              #If everything is correct then print well formed.
	print "Well formed"
		
		
