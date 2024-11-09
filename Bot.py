print("\033[0;32;40m Hello sir welcome to FLYZONE84 \n")
print("\033[0;33;40m What is you'r beautifull name sir \n")
name = input("                                 :")
if name == "" :
	print ("\033[0;31;40m Name is required !!!!!! \n")
	name  = input (" What is you'r name ? : ")
print("\n")
gender = input ("\033[0;32;40m what is you'r gender :")
if gender == "male":
	print("\n")
	print ("hey Gentle man \n")
	Age = input ("\033[0;34;40m How old are you : ")
	
elif gender == "female":
	print("\n")
	print ("hey madam \n")
	Age = input ("\033[0;34;40m How old are you : ")

if Age == "" :
	print("\n")
	print ("\031[0;33;40m AGE is required !!!!!! \n")
	
print("\033[0;31;50m Sorry " + name +" FLYZONE84 not woeking with you !!!!!!!!!  \n")
