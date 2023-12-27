import os
import time, datetime
import mysql.connector
import pyfiglet
from pyfiglet import figlet_format
import colorama
from colorama import Fore, Back, Style

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
Use `{Fore.GREEN}--create {Fore.YELLOW}[Account username] {Fore.RED}[password]{Style.RESET_ALL}, after it
use `{Fore.GREEN}--start{Style.RESET_ALL}` then to login use, `--login [username] [password]`
Enjoy your forums,

Acknowledgement :
To Start Post use `-e` or `--post`, to delete your post `-pd [messageID]` or
`--post_delete [messageID]` or `--delete [messageID]`. only admin has access
to your message, and can delete it. or maybe deactivating your account.
    """
    return description
  
  
def Lexer():
  print(Figlet.header())
  time.sleep(1)
  print(Figlet.description())
  
  
Lexer()