import builtwith
import os
import pyfiglet
os.system('cls'or'clear')
class color:
    RED = "\033[31m"
    BLUE = "\033[34m"
    GREEN = "\033[32m"
    END = "\033[97m"
result = pyfiglet.figlet_format("CMS",font='standard')
print(result)
print(color.GREEN+"Made By Reza Moradi"+color.END)

url = str(input("Enter A Domain ==> "))
if 'http://' or 'https://' not in url:
    url = f'http://{url}'
else:
    pass
target = builtwith.parse(url)

for name in target:
    for val in target[str(name)]:
        print(name+" : "+val)
    
a = str(input("\nPress (ENTER) To Go To Main Menu... "))
if a == '':
    import Hack_Tools
else:
    print(color.RED+f"{a} Not Found"+color.END)
