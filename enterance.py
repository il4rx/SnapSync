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
import sys

date = datetime.datetime.now()
_strf = date.strftime("%x")
_connector = mysql.connector.connect(
    host="localhost", user="root", password="", database="snap_snyc"
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

Acknowledgement :
To Start Post use {Fore.GREEN}-e{Style.RESET_ALL} or {Fore.GREEN}--post{Style.RESET_ALL}, to delete your post {Fore.GREEN}-pd {Fore.YELLOW}[messageID]{Style.RESET_ALL} or
{Fore.GREEN}--post_delete {Fore.YELLOW}[messageID]{Style.RESET_ALL} or {Fore.GREEN}--delete {Fore.YELLOW}[messageID]{Style.RESET_ALL}. only admin has access
to your message, and can delete it. or maybe deactivating your account.
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
            time.sleep(3)
            query = "INSERT INTO `users`(`user_id`, `username`, `password`, `date`) VALUES (%s, %s, %s,%s)"
            params = (user_id, username, hashed_password, _strf)
            _cursor.execute(query, params)
            _connector.commit()
        finally:
            print("Your Account Successfully Created!")
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

def main():
    Figlet.header()
    Figlet.description()
    Main.body()
  

if __name__ == "__main__":
    main()
