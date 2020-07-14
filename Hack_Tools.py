import os
import pyfiglet
import time


os.system('cls'or'clear')

class color:
    RED = "\033[31m"
    BLUE = "\033[34m"
    GREEN = "\033[32m"
    END = "\033[97m"
os.system('cls' or 'clear')
result = pyfiglet.figlet_format('Hack Tools')

print(color.GREEN +f"{result} v1.0" )
print(color.RED + 'Made By Reza Moradi\n\n'+color.BLUE)
print("[1] Port Scanner\n")
time.sleep(0.2)
print("[2] IP Finder\n")
time.sleep(0.2)
print("[3] IP Information\n")
time.sleep(0.2)
print("[4] CloudFlare Bypass\n")
time.sleep(0.2)
print("[5] CMS\n")
time.sleep(0.2)
print("[6] Admin Page Finder\n")
time.sleep(0.2)
print("[7] Reverse IP\n")
time.sleep(0.2)
print("[8] Whois\n")
time.sleep(0.2)
choose = str(input("\n==>"))

if choose == '1':
    import portscanner
elif choose == '2':
    import IP_Finder
elif choose == '3':
    import IP_INFO
elif choose == '4':
    import cloudflare
elif choose == '5':
    import cms
elif choose == '6':
    import admin_page
elif choose == '7':
    import reverse_ip
elif choose == '8':
    import who_is
else:
    print("None Command!!!")
