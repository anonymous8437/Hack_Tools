import socket
import os
import pyfiglet
def ip():
    class color:
        RED = "\033[31m"
        GREEN = "\033[32m"
        END = "\033[97m"
    os.system("cls" or 'clear')

    result = pyfiglet.figlet_format("IP Finder", font = 'standard')
    print(result)
    print(color.RED + "Made By Reza Moradi"+color.END)
    print(" ")
    URL = input(color.GREEN + "Enter A URL: "+color.END )




    ip = socket.gethostbyname(URL)
    print(color.END+"\n"+ip)
    a = str(input("\nPress (ENTER) To Go To Main Menu... "))
    if a == '':
        import Hack_Tools
    else:
        print(color.RED+f"{a} Not Found"+color.END)

ip()