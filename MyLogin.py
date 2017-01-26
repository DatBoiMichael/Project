import datetime
import sys 
import re

now = datetime.datetime.now()
login = now.strftime("%A""%m""%Y")



file = open("passw.rtf","r")
whole_text = file.readlines()
listed_text = re.findall('[A-Z][^A-Z]*', str(whole_text))


def callLogin():
	
	eight = ["Monday","Tuesday","Wednesday"]
	

	for i in eight: 
		if i in login:
			pass1 = 8 
			

	nine = ["Thursday","Friday"]
	for q in nine: 
		if q in login:
			pass1 = 9
			

	ten = ["Saturday","Sunday"]
	for x in ten: 
		if x in login: 
			pass1 = 10

	return pass1



def cracker():

	constraints = ["!","@","£","$","%","&","*","#"]
	numrules = callLogin()
	
	for index in listed_text:
		if len(index) == numrules:
			if index != constraints:
				print ('The password is: ',index)


print("Your login is: ",login)
cracker()



#will be the length of callLogin()
#password start with a capital letter 
#is not equals to !,@,£,$,%,&,*,#
			








    

	






