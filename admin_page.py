import os
import requests
import pyfiglet

os.system("cls"or"clear")
class color:
    RED = "\033[31m"
    BLUE = "\033[34m"
    GREEN = "\033[32m"
    END = "\033[97m"
result = pyfiglet.figlet_format("Admin Page Finder",font='standard')
print(result+color.GREEN+"Made By Reza Moradi"+color.END)
pages = ['admin','admin.php','admin.html','admin1','admin1.php','wp-admin','adm','administrator']
url = str(input(color.BLUE+"Enter a URL: ==> "+color.END))
if 'http://' or 'https://' not in url:
    url = 'http://'+url
else:
    pass
for page in pages:
    r = requests.get(url+"/"+page)
    if r.status_code == 200:
        print(color.GREEN+f"{url}/{page}    Found"+color.END)
    else:
        print(color.RED+f'{url}/{page}  Not Found'+color.END)
a = str(input("\nPress (ENTER) To Go To Main Menu... "))
if a == '':
    import Hack_Tools
else:
    print(color.RED+f"{a} Not Found"+color.END)
