import os
import socket
import time
import pyfiglet

class color:
    RED = "\033[31m"
    BLUE = "\033[34m"
    GREEN = "\033[32m"
    END = "\033[97m"

os.system('cls' or 'clear')

result = pyfiglet.figlet_format('CloudFlare Bypass',font = 'standard')
print(result)
print(color.RED+"Made By Reza Moradi\n")
subdom = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']
site = str(input(color.BLUE+"Enter a Site Domain: ==>"))
if site == '':
    try:
        site = str(input(color.BLUE+"Enter a Site Domain: ==>"))
    except:
        print(color.RED+"Please Enter Any Thing!!!")
for sub in subdom:
    try:
        ip = socket.gethostbyname(str(sub)+'.'+str(site))
        print(str(sub)+'.'+str(site)+'  ==>  '+ip)
    except Exception:
        pass

a = str(input("\nPress (ENTER) To Go To Main Menu... "))
if a == '':
    import Hack_Tools
else:
    print(color.RED+f"{a} Not Found"+color.END)