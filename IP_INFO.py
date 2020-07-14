import requests
import os
import pyfiglet

def IP_INFO():
    class color:
        RED = "\033[31m"
        GREEN = "\033[32m"
        BLUE = "\033[34m"
        WHITE = "\033[97m"


    os.system("cls" or 'clear')
    result = pyfiglet.figlet_format('IP Information',font = 'standard')
    print(color.RED + result)
    print(color.BLUE + "Made By Reza Moradi\n")

    ip = str(input(color.GREEN+"Enter A IP: ==> "+color.WHITE))
    try:

        r = requests.get(f'https://ipapi.co/{ip}/json/').json()
        ip = ip
        city = r['city']
        region = r['region']
        country = r['country_name']
        capital = r['country_capital']
        timezone = r['timezone']
        currency = r['currency_name']
        lang = r['languages']
        org=r['org']
        print(f"IP : {ip}")
        print(f"City : {city}")
        print(f"Region : {region}")
        print(f"Country : {country}")
        print(f"Capital : {capital}")
        print(f"Timezone : {timezone}")
        print(f"Currency : {currency}")
        print(f"Language : {lang}")
        print(f"Org : {org}")
    except:
        print("Can't Connect!\nCheck Your Connection And Try Again.")
    a = str(input("\nPress (ENTER) To Go To Main Menu... "))
    if a == '':
        import Hack_Tools
    else:
        print(color.RED+f"{a} Not Found"+color.END)
IP_INFO()