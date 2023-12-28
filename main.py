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
import json

date = datetime.datetime.now()
_strf = date.strftime("%x")
_connector = mysql.connector.connect(
    host="localhost", user="root", password="", database="snap_snyc"
)
_cursor = _connector.cursor()
class Fallback :
    def __init__(self) -> None :
        print("Fallback In Process....")
        time.sleep(1)
        os.system("cls||clear")
        subprocess.Popen(["python", "enterance.py"])
        sys.exit(0)
        
class MainBody :
    def __init__(self) :
        print(f"""@ Hello, Welcome To SnapSync Forums,
If You New Here, Please Login First, Maybe
You're not creating your account yet,
That's why you need to start from 
{Fore.GREEN}enterance.py{Style.RESET_ALL} you can 
fall back using --fallback, please
login using --login!      
              """)
        
        time.sleep(1)
        userInput = input(">>> ")
        
        
        if userInput == "--fallback" :
            Fallback()
        elif userInput == "--login" : 
            userTaskInput = input("Username : >>> ")
            try :
                print('Finding username....')
                time.sleep(3)
                sql = "SELECT * FROM users WHERE username = %s"
                
                _cursor.execute(sql, (userTaskInput, ))
                _result = _cursor.fetchall()
                
                if len(_result) < 1 :
                    print("Username not found!")
                    time.sleep(1)
                    os.system("cls||clear")
                    subprocess.Popen(["python", "enterance.py"])
                    sys.exit(0)
                else :
                    userPasswordInput = str(input("Password : >>> "))
                    
                    for result in _result:
                        hashed_password = str(result[2])
                        userId = str(result[0])
                        username = str(result[1])
                        
                        if bcrypt.checkpw(userPasswordInput.encode('utf-8'), hashed_password.encode('utf-8')):
                            
                            
                            with open('./Auth/Auth.json', "r+") as OAuth2 :
                                _AuthData = json.load(OAuth2)
                                _AuthData['userID'] = userId
                                _AuthData["username"] = username
                            
                                OAuth2.seek(0)
                                json.dump(_AuthData, OAuth2)
                                OAuth2.truncate()
                                
                            print('Succeed!')
                            time.sleep(1)
                            
                        else:
                            print("Password Wrong!")
                            time.sleep(1)
                            os.system("cls||clear")  # Improved cross-platform clear
                            subprocess.Popen(["python", "enterance.py"])
                            sys.exit(0)
                    
            except ValueError :
                print("Error, Value is Missing!")
                
                
with open('./Auth/Auth.json', "r") as JsonFile :
    AuthData = json.load(JsonFile)
    if len(AuthData) < 1 or len(AuthData) == 0 :
        MainBody()
    else :
        print('You already logged!')
        time.sleep(1)