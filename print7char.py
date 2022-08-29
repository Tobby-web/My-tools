#this code is to convert the  files toa a list 
with  open("/home/kali/tools/common_passwords.txt")  as file:
	lines   =  file.readlines()
	lines = [line.rstrip() for line in lines]
#print (lines)

#here, we're going to loop the data in the list and count them
for i in lines:
	if len(i) == 7:
		print (i)



