import os
import time, datetime
import mysql.connector
import pyfiglet


_connector = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="snap_snyc"
)

