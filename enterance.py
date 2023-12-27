import os
import time, datetime
import mysql.connector
import pyfiglet
from pyfiglet import figlet_format
import colorama
from colorama import Fore, Back, Style
import bcrypt
import random
import subprocess
import sys

date = datetime.datetime.now()
_strf = date.strftime("%x")


_connector = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="snap_snyc"
)

_cursor = _connector.cursor()


class Figlet :
  def header() :
    figlet = figlet_format("SnapSync")
    return figlet
  def description() :
    description = f"""
Welcome to SnapSync, You Can Create Your Account Here,
Use `{Fore.GREEN}--create{Style.RESET_ALL}, after it
use `{Fore.GREEN}--start{Style.RESET_ALL}` then to login use, `{Fore.GREEN}--login{Style.RESET_ALL}
Enjoy your forums,

Acknowledgement :
To Start Post use `{Fore.GREEN}-e{Style.RESET_ALL}` or `{Fore.GREEN}--post{Style.RESET_ALL}`, to delete your post `{Fore.GREEN}-pd {Fore.YELLOW}[messageID]{Style.RESET_ALL}` or
`{Fore.GREEN}--post_delete {Fore.YELLOW}[messageID]{Style.RESET_ALL}` or `{Fore.GREEN}--delete {Fore.YELLOW}[messageID]{Style.RESET_ALL}`. only admin has access
to your message, and can delete it. or maybe deactivating your account.
    """
    return description


class Main :
  def Body() :
    print(f"{Fore.CYAN}[+]{Style.RESET_ALL} Please Input Any Commands")
    userInput = input(">>> ")

    if userInput == "--create":
      username_input = input("Username : >>> ")
      password_input = input("Password : >>> ")
      
      password_input = password_input.encode('utf-8')
      password_hash = bcrypt.hashpw(password_input, bcrypt.gensalt(10))
      user_ids = int(f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}")
      
      try :
        print("Creating Account...")
        time.sleep(5)
        
        prompt = "INSERT INTO `users`(`user_id`, `username`, `password`, `date`) VALUES (%s, %s, %s,%s)"
        values = (user_ids, username_input, password_hash, _strf)
        _cursor.execute(prompt, values)
        _connector.commit()
        
      finally :
        print("Your Account Successfully Created!")
        time.sleep(2)
    pass
  
    if userInput == "--start":
      print("ok")
    
    
    
def Lexer():
  while True:
    print(Figlet.header())
    time.sleep(1)
    print(Figlet.description())
    time.sleep(1)
    
    Main.Body()
    os.system("cls||clear")
  
Lexer()