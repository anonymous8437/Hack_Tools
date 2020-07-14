import os
import whois
import pyfiglet

class color:
    RED = "\033[31m"
    BLUE = "\033[34m"
    GREEN = "\033[32m"
    END = "\033[97m"
os.system("cls"or'clear')
result = pyfiglet.figlet_format("Whois",font = 'standard')
print(result+'\n'+color.BLUE+'Made By Reza Moradi'+color.RED+'\n')
site = whois.whois(str(input(color.RED+"Enter a Domain ==> "+color.GREEN)))
print(f'\n {site.text}')
a = str(input("\nPress (ENTER) To Go To Main Menu... "))
if a == '':
    import Hack_Tools
else:
    print(color.RED+f"{a} Not Found"+color.END)