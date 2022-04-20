import requests
from colorama import Fore,init
import random
init(convert=True)
import os,sys
import pyfiglet


os.system("title Support : t.me/terminaluwu")


def cls():
    linux = "clear"
    windows = "cls"
    os.system([linux,windows][os.name=="nt"])

def sniper_proxied():
    r = requests.patch('https://discord.com/api/v9/guilds/'+server_id+'/vanity-url',proxies="http://"+random.choice(proxy),headers={'Authorization': token},json={'code': vanity})
    if r.status_code == 200:
        print(Fore.GREEN+"Vanity Succesfully Sniped"+ Fore.RESET)
    else:
        print(Fore.RED+"Failed to snipe vanity"+Fore.RESET)

def sniper_proxyless():
    r = requests.patch('https://discord.com/api/v9/guilds/'+server_id+'/vanity-url',headers={'Authorization': token},json={'code': vanity})
    if r.status_code == 200:
        print(Fore.GREEN+"Vanity Succesfully Sniped"+ Fore.RESET)
        sys.exit()
    else:
        print(Fore.RED+"Failed to snipe vanity"+Fore.RESET)


cls()

banner = pyfiglet.figlet_format("Vanity  Sniper")
print(Fore.LIGHTMAGENTA_EX+banner+Fore.RESET)
token_type = input(Fore.LIGHTCYAN_EX+"Do you want to use [1] Proxied [2] Proxyless : "+Fore.RESET)
server_id = input(Fore.LIGHTCYAN_EX+"\n \n Please Enter the server id : "+Fore.RESET)
token = input(Fore.LIGHTCYAN_EX+"\n \n Please Enter the Token : "+Fore.RESET)
vanity = input(Fore.LIGHTCYAN_EX+"\n \n Please Enter the vanity to snipe : "+Fore.RESET)
p = print(Fore.LIGHTGREEN_EX+"Press Any Key to Start the Sniper..."+Fore.RESET)
if token_type == "1":
    proxy = open('proxies.txt').read().split('\n')
    cls()
    while True:
        sniper_proxied()
elif token_type == "2":
    cls()
    while True:
        sniper_proxyless()
    
