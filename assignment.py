#!python

"""
Create a program that will store the database for a veterinary
Each record needs to have the following information:


id unique integer identifier
pet name
pet species (cat, bird, dog, etc)
pet breed (persian, beagle, canary, etc)
owner name
owner phone number
owner email
owner balance (amount owing)
date of first visit

create a program that will allow the user to:
insert a new record into the database and save it automatically
retrieve a record by their id and display all of the information
retrieve a record by the email and display all of the information
retrieve a record by phone number and display all of the information

You will need to create the table yourself. Consider what data types you will
need to use.
"""
import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
query = "select sqlite_version();"

query = "drop table if exists veterinary"
cursor.execute(query)

query = """create table veterinary 
( 
id integer primary key autoincrement, 
petname tinytext,
petspecies tinytext,
petbreed tinytext, 
ownername tinytext,
phoneNumber int, 
email tinytext,
balance int,
date int); """

cursor.execute(query)

def insert_record():
    petname = input("Enter pet name: ")
    petspecies = input("Enter pet species: ")
    petbreed = input("Enter pet breed: ")
    ownername = input("Enter owner's name: ")
    phoneNumber = input("Enter phone number: ")
    email = input("Enter email address: ")
    balance = float(input("Enter balance: "))
    date = input("Enter date of first visit (YYYY-MM-DD): ")
    
    cursor.execute('''
        INSERT INTO pets (petname, petspecies, petbreed, ownername, phoneNumber, email, balance, date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (petname, petspecies, petbreed, ownername, phoneNumber, email, balance, date))
connection.commit()
cursor.execute(query)
print("it worked")

query = "select * from customers"
cursor.execute(query)
result = cursor.fetchall()

for i in result:
    print(i)
