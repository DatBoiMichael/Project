import datetime
import sys 
import re


#define datetime.now() from datetime module into the now variable. The now
#variable now has the functionalities of datetime.now() function. The strftime 
#is just another function from datetime where you can choose the values from
#that function. The values being "%A" which is the day in capital, "%m" is month
#in numerics "%Y" is equal to year

now = datetime.datetime.now()
login = now.strftime("%A""%m""%Y")

#open the file, store it to varible called file and "r" means read. You can
#choose "w" if you want to write on it. You use the readline() function to store
#the whole text from the file into as 1 element inside a list i.e. ['DrtirttsFererreiEddkfd']
#The value from the function findall '[A-Z][^A-Z]*' means find all the capitals
#and it will split every word that starts with a capital from the file in the variable
#whole_text that had its data-type changed into a string. 


file = open("test.txt","r")
whole_text = file.readlines()
listed_text = re.findall('[A-Z][^A-Z]*', str(whole_text))

#This function has 3 list eight, nine and ten. There are 3 for loops that go through each 
#list i.e. for i in eight , i means any element in the list eight, if one of the element
#matches with the string in login then it will store 8 to pass1

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

#This function calls the on another function callLogin() and assigns it to numrules
#The constraints are in the list. Then it goes thru each element in listed_text which is
#located at the top of the page. At this point in listed_text the strings were already split
# where string starts with a capital letter i.e. ['Drtirtts', 'Fererrei', 'Eddkfd']. The if statement
#len(index) counts the number of character in any element for example 'Drtirtts' has
# 8 and if thats is equal to the 'pass1' value in the numrules value then a nested condition
#is followed by checking if its not equal to any of those constraints in the list then print that index

def cracker():

	constraints = ["!","@","£","$","%","&","*","#"]
	numrules = callLogin()
	
	for index in listed_text:
		if len(index) == numrules:
			if index != constraints:
				print ('The password is: ',index)



#Then you just the cracker()function and it prints out value of that index that matches
#the constraints and conditions.
				
print("Your login is: ",login)
cracker()



#rules of password: 
#will be the length of callLogin()
#password start with a capital letter 
#is not equals to !,@,£,$,%,&,*,#
			








    

	






