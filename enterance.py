import os
import time
import datetime
import mysql.connector
import pyfiglet
import colorama
from colorama import *
import bcrypt
import random
import subprocess
import json
import sys
import pathlib


date = datetime.datetime.now()
_strf = date.strftime("%x")
_connector = mysql.connector.connect(
    host="localhost", user="root", password="", database="snap_sync"
)
_cursor = _connector.cursor()

class Figlet:
    @staticmethod
    def header():
        return pyfiglet.figlet_format("SnapSync")

    @staticmethod
    def description():
        return f"""
Welcome to SnapSync, You Can Create Your Account Here,
Use {Fore.GREEN}--create{Style.RESET_ALL} to create your account or make a new account, after it
use {Fore.GREEN}--start{Style.RESET_ALL}, to start the forum (you need to log in again)
"""

class Main:
    @staticmethod
    def create_account():
        username = input("Username : >>> ")
        password = input("Password : >>> ")
        password = password.encode("utf-8")
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(10))
        user_id = f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"
        try:
            print("Creating Account...")
            time.sleep(1)
            sqli = "SELECT * FROM users WHERE username = %s"
            _cursor.execute(sqli, (username,))
            _result = _cursor.fetchall()
            _role = "User"
            if len(_result) < 0 or len(_result) == 0 :
                query = "INSERT INTO `users`(`user_id`, `username`, `password`, `role`, `date`) VALUES (%s, %s, %s,%s, %s)"
                params = (user_id, username, hashed_password, _role, _strf)
                _cursor.execute(query, params)
                _connector.commit()
                
                with open("./Auth/Auth.json", "r+") as OAuth2:
                    _AuthData = json.load(OAuth2)
                    _AuthData["userID"] = user_id
                    _AuthData["username"] = username

                    OAuth2.seek(0)
                    json.dump(_AuthData, OAuth2)
                    OAuth2.truncate()

                print("Your Account Successfully Created!")
                time.sleep(3)
            else :
                print('The username is already used by someone else!')
                time.sleep(5)
                
        except ValueError:
            time.sleep(2)

    @staticmethod
    def start_program():
        try:
            print("Starting Program....")
            time.sleep(1)
            os.system("cls||clear")
            subprocess.Popen(["python", "main.py"])
            sys.exit(0)
        except KeyboardInterrupt:
            print("Error!")

    @staticmethod
    def body():
        while True:
            print(Figlet.header())
            time.sleep(1)
            print(Figlet.description())
            time.sleep(1)
            print(f"{Fore.CYAN}[+]{Style.RESET_ALL} Please Input Any Commands")
            command = input(">>> ")
            if command == "--create":
                Main.create_account()
                os.system("cls||clear")
            elif command == "--start":
                os.system("cls||clear")
                Main.start_program()
            else:
                print("Invalid command")
                time.sleep(1)
                os.system("cls||clear")

def main():
    Figlet.header()
    Figlet.description()
    Main.body()


class Lexer:
    def __init__(self) -> None:
        os.system("cls||clear")
        subprocess.Popen(["python", "enterance.py"])
        sys.exit(0)




class Authenticated() :
    def __init__(self) :
        print(f"You Have Been Authenticated,\nYou Couldn't Create A New Account\nWhen You Still Login,\nPlease Log Out First!\nUse {Fore.GREEN}`--logout`{Style.RESET_ALL} to logout!\n")
        
        command_prompt = input(f"{Fore.CYAN}>>>{Style.RESET_ALL} // ")
        
        if command_prompt == "--logout" :
                print('Try to logout...')
                time.sleep(1)
                with open("./Auth/Auth.json", "r+") as Jsons:
                    AuthDat = json.load(Jsons)
                    AuthDat = {}
                    Jsons.seek(0)
                    json.dump(AuthDat, Jsons)
                    Jsons.truncate()
                
                Lexer()
        else : 
            print("Invalid argument!")
        time.sleep(2)

if __name__ == "__main__":
    with open("./Auth/Auth.json", "r") as JsonFile:
        AuthData = json.load(JsonFile)
        if len(AuthData) < 1 or len(AuthData) == 0:
            main()
        else:
            os.system("cls||clear")
            Authenticated()
            time.sleep(1)

