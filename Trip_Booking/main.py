import os

import mysql.connector as sqlc

# print(os.environ.get("DB_PASSWORD"))
keshav_con = sqlc.connect(host = "localhost", user = "root",passwd = "keshav24") # here i connected it to my database

cursor = keshav_con.cursor() # cursor to execute queries

def execute(query):
    cursor.execute(query)
execute("show databases")

data = cursor.fetchone()
print(data)

# python3 main.py
