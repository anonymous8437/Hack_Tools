import socket
import pyfiglet
import os
def portscan():
    class color:
        GREEN = '\033[32m'
        RED = '\033[31m'
        END = '\033[39m'
        BLUE = '\033[34m'
        YELLOW = '\033[33m'
    os.system('cls' or 'clear')

    result = pyfiglet.figlet_format('Port Scanner',font = 'standard')
    print(result)
    print( color.YELLOW + "Made By Reza Moradi\n" + color.BLUE)
    ip = input(color.BLUE + "Enter a IP To Scan: ")
    port_list=[]
    for port in range(1,5000):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = s.connect_ex((ip,port))
        if result == 0:
            print(f"{color.BLUE}{ip}:{port}     {color.GREEN}open{color.END}    [ open ports: {color.GREEN}{port_list}{color.END} ]")
            print("-"*60)
            port_list.append(port)
        else:
            print(f"{color.BLUE}{ip}:{port}     {color.RED}close{color.END}    [ open ports: {color.GREEN}{port_list}{color.END} ]")
            print("-"*60)
    a = str(input("\nPress (ENTER) To Go To Main Menu... "))
    if a == '':
        import Hack_Tools
    else:
        print(color.RED+f"{a} Not Found"+color.END)
portscan()