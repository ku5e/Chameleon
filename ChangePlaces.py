#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: XX/XX/XXXX
#Purpose: Change computer name
import os
import time
import random
from dotenv import load_dotenv

#get password from env
load_dotenv()
password = os.environ.get('PASSWORD')

#read possible names from file
textfile = 'namelist.dat'
text = open('namelist.dat', 'r')
names = text.readlines()

newName = random.choice(names)

#Change MAC
#read possible macs from list
textfile = 'macs.dat'
text = open('macs.dat', 'r')
macs = text.readlines()

macChoice = random.choice(macs)

macPre, brand = macChoice[:8], macChoice[11:]

hexNums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
macPost = (':' + random.choice(hexNums) + random.choice(hexNums) +
	':' + random.choice(hexNums) + random.choice(hexNums) +
	':' + random.choice(hexNums) + random.choice(hexNums))

mac = macPre + macPost

#set new mac address
os.system('/usr/bin/sudo /sbin/ifconfig en0 down')
time.sleep(1)
os.system('/bin/echo ' + password + ' | /usr/bin/sudo -S ifconfig en0 link ' + mac)
print() 
time.sleep(1)

#Change name
os.system('/usr/bin/sudo scutil --set ComputerName ' + newName)
time.sleep(1)
os.system('/usr/bin/sudo scutil --set LocalHostName ' + newName)
time.sleep(1)
os.system('/usr/bin/sudo scutil --set HostName ' + newName)

#Restart Networking

os.system('/usr/bin/sudo /sbin/ifconfig en0 up')
# to check if back up ifconfig -u en0


print('Your new name is', newName)
print('You are now a ' + brand + ' with the address of \n' + mac)
