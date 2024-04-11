#usr/bin/python

from colorama import Fore
from time import sleep
import requests
import os

red = Fore.RED
blue = Fore.BLUE
cyan = Fore.CYAN
green = Fore.GREEN
reset = Fore.RESET
lyellow = Fore.LIGHTYELLOW_EX

def banner():
    os.system("clear" or "cls")
    print(cyan + """
  ___      _             
 |   \ _ _(_)_ _____ _ _ 
 | |) | '_| \ V / -_) '_|
 |___/|_| |_|\_/\___|_|  

            coded by driver 
            version 1.0
          
          help --> -h
""" + reset)
    sleep(1)
    while True:
      user_input = input(green + "  >>"+ reset)
      sleep(1)
    
banner()
