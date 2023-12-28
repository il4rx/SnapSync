import os
import datetime
import mysql.connector
import pyfiglet
from pyfiglet import figlet_format
import colorama
from colorama import Fore, Back, Style
import bcrypt
import time
import random
import subprocess
import sys
import json

date = datetime.datetime.now()
_strf = date.strftime("%Y-%m-%d %H:%M:%S")

_connector = mysql.connector.connect(
    host="localhost", user="root", password="", database="snap_sync"
)
_cursor = _connector.cursor()


class Fallback:
    def __init__(self) -> None:
        print("Fallback In Process....")
        os.system("cls||clear")
        subprocess.Popen(["python", "enterance.py"])
        sys.exit(0)


class Lexer:
    def __init__(self) -> None:
        os.system("cls||clear")
        subprocess.Popen(["python", "main.py"])
        sys.exit(0)


class MainBody:
    def __init__(self):
        print(
            f"""@ Hello, Welcome To SnapSync Forums,
If You New Here, Please Login First, Maybe
You're not creating your account yet,
That's why you need to start from 
{Fore.GREEN}enterance.py{Style.RESET_ALL} you can 
fall back using --fallback, please
login using --login!      
              """
        )

        userInput = input(">>> ")

        if userInput == "--fallback":
            Fallback()
        elif userInput == "--login":
            userTaskInput = input("Username : >>> ")
            try:
                print("Finding username....")
                sql = "SELECT * FROM users WHERE username = %s"

                _cursor.execute(sql, (userTaskInput,))
                _result = _cursor.fetchall()

                if len(_result) < 1:
                    print("Username not found!")
                    os.system("cls||clear")
                    subprocess.Popen(["python", "enterance.py"])
                    sys.exit(0)
                else:
                    userPasswordInput = str(input("Password : >>> "))

                    for result in _result:
                        hashed_password = str(result[2])
                        userId = str(result[0])
                        username = str(result[1])

                        if bcrypt.checkpw(
                            userPasswordInput.encode("utf-8"), hashed_password.encode("utf-8")
                        ):
                            with open("./Auth/Auth.json", "r+") as OAuth2:
                                _AuthData = json.load(OAuth2)
                                _AuthData["userID"] = userId
                                _AuthData["username"] = username

                                OAuth2.seek(0)
                                json.dump(_AuthData, OAuth2)
                                OAuth2.truncate()
                            
                            Lexer()
                        else:
                            print("Password Wrong!")
                            os.system("cls||clear")  # Improved cross-platform clear
                            subprocess.Popen(["python", "enterance.py"])
                            sys.exit(0)
            except ValueError:
                print("Error, Value is Missing!")
                time.sleep(4)


class Authenticated:
    def __init__(self):
        sql_member = "SELECT * FROM users WHERE username = %s"
        with open("./Auth/Auth.json", "r") as JsonsFile:
            AuthData = json.load(JsonsFile)
            
            _cursor.execute(sql_member, (AuthData['username'],))
            member_res = _cursor.fetchall()
            
            username_format = f"{Fore.LIGHTBLUE_EX}{AuthData['username']}{Style.RESET_ALL}"
            for membros in member_res :
                username_with_indicators = f"🛠️ {username_format}" if membros[3] == "Admin" else f"👑 {username_format}" if membros[3] == "Owner" else f"{username_format}"
            
            
            print(f"@ Welcome {username_with_indicators} \n")
            sql_data = "SELECT * FROM chat ORDER BY id DESC LIMIT 20"
            
            _cursor.execute(sql_data)
            data_res = _cursor.fetchall()
            
            
            

            if len(data_res) < 0 or len(data_res) == 0:
                print("No One's Post Anything, Or Discuss Anything Here!")
            else:
                for msg in data_res:
                    username_formats = f"{Fore.LIGHTBLUE_EX}{msg[1]}{Fore.LIGHTGREEN_EX} [{msg[2]}]{Style.RESET_ALL}"
                    userIndicator = f"🛠️ {username_formats}" if msg[2] == "Admin" else f"👑 {username_formats}" if msg[2] == "Owner" else f"{username_formats}"
                    print(
                        f"{userIndicator} : {msg[4]} {Fore.LIGHTBLACK_EX}({msg[5]}) {Fore.MAGENTA}[{msg[3]}]{Style.RESET_ALL}"
                    )
                print("\n\n")
            command_prompt = input(f"{Fore.CYAN}>>>{Style.RESET_ALL} // ")

            if command_prompt == "--fallback":
                Fallback()
            elif command_prompt == "--refresh" :
                Lexer()
            elif command_prompt == "--logout" :
                print('Try to logout...')
                with open("./Auth/Auth.json", "r+") as Jsons:
                    AuthDat = json.load(Jsons)
                    AuthDat = {}
                    Jsons.seek(0)
                    json.dump(AuthDat, Jsons)
                    Jsons.truncate()
                    Fallback()
            else:
                with open("./Auth/Auth.json", "r") as JsonAuth:
                    Json_Auth = json.load(JsonAuth)
                    
                    
                content_id = f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"
                sql = "SELECT * FROM users WHERE username = %s"
                _cursor.execute(sql, (Json_Auth["username"],))
                cbtresult = _cursor.fetchall()
                
                try:
                    print("Posting....")
                    sql_query = "INSERT INTO `chat`(`id`, `username`, `user_role`, `content_id`, `contents`, `datetime`) VALUES ('',%s,%s,%s,%s,%s)"
                    for res in cbtresult :
                        psurname = res[1]
                        userRole = res[3]
                    params = (psurname, userRole, content_id, command_prompt, _strf)
                    _cursor.execute(sql_query, params)
                    _connector.commit()
                finally:
                    Lexer()


with open("./Auth/Auth.json", "r") as JsonFile:
    AuthData = json.load(JsonFile)
    if len(AuthData) < 1 or len(AuthData) == 0:
        MainBody()
    else:
        os.system("cls||clear")
        Authenticated()
