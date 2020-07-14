import requests
import os
import pyfiglet
os.system('cls'or'clear')
class color:
    RED = "\033[31m"
    BLUE = "\033[34m"
    GREEN = "\033[32m"
    END = "\033[97m"

result = pyfiglet.figlet_format('Reverse IP',font='standard')
print(result)
print(color.BLUE+"Made By Reza Moradi\n"+color.END)
site=input(color.GREEN+"Enter a IP/Domain ==> "+color.END)
data = {'remoteAddress':site}
r = requests.post("https://domains.yougetsignal.com/domains.php",data).json()

for site in r['domainArray']:
    print(site[0])

a = str(input("\nPress (ENTER) To Go To Main Menu... "))
if a == '':
    import Hack_Tools
else:
    print(color.RED+f"{a} Not Found"+color.END)
