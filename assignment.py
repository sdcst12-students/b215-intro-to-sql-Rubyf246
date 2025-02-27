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
cumid int,
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
    cumid = float(input("Enter your ID: "))
    petname = input("Enter pet name: ")
    petspecies = input("Enter pet species: ")
    petbreed = input("Enter pet breed: ")
    ownername = input("Enter owner's name: ")
    phoneNumber = input("Enter phone number: ")
    email = input("Enter email address: ")
    balance = float(input("Enter balance: "))
    date = input("Enter date of first visit (YYYY-MM-DD): ")
    
    cursor.execute('''
        INSERT INTO pets (cumid, petname, petspecies, petbreed, ownername, phoneNumber, email, balance, date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (cumid, petname, petspecies, petbreed, ownername, phoneNumber, email, balance, date))
connection.commit()

def retrieve_by_id():
    Cumid = int(input("Enter ID: "))
    cursor.execute('''
        SELECT * FROM veterinary WHERE cumid = ?
    ''', (Cumid,))
    record = cursor.fetchone()
    if record:
        print("Record found:")
        print(f"Cusutomers ID: {record[0]}")
        print(f"Pet Name: {record[1]}")
        print(f"Species: {record[2]}")
        print(f"Breed: {record[3]}")
        print(f"Owner Name: {record[4]}")
        print(f"Owner Phone: {record[5]}")
        print(f"Owner Email: {record[6]}")
        print(f"Owner Balance: ${record[7]}")
        print(f"First Visit Date: {record[8]}")
    else:
        print("No record found with that ID.")

def retrieve_by_email():
    owner_email = input("Enter owner's email address: ")
    cursor.execute('''
        SELECT * FROM pets WHERE email = ?
    ''', (owner_email,))
    record = cursor.fetchone()
    if record:
        print("Record found:")
        print(f"ID: {record[0]}")
        print(f"Pet Name: {record[1]}")
        print(f"Species: {record[2]}")
        print(f"Breed: {record[3]}")
        print(f"Owner Name: {record[4]}")
        print(f"Owner Phone: {record[5]}")
        print(f"Owner Email: {record[6]}")
        print(f"Owner Balance: ${record[7]}")
        print(f"First Visit Date: {record[8]}")
    else:
        print("No record found with that email.")

def retrieve_by_phone():
    owner_phone = input("Enter owner's phone number: ")
    cursor.execute('''
        SELECT * FROM pets WHERE phoneNumber = ?
    ''', (owner_phone,))
    record = cursor.fetchone()
    if record:
        print("Record found:")
        print(f"ID: {record[0]}")
        print(f"Pet Name: {record[1]}")
        print(f"Species: {record[2]}")
        print(f"Breed: {record[3]}")
        print(f"Owner Name: {record[4]}")
        print(f"Owner Phone: {record[5]}")
        print(f"Owner Email: {record[6]}")
        print(f"Owner Balance: ${record[7]}")
        print(f"First Visit Date: {record[8]}")
    else:
        print("No record found with that phone number.")

# Main menu
def menu():
    while True:
        print("\nWelcome to the Veterinary Database")
        print("1. Insert a new record")
        print("2. Retrieve a record by ID")
        print("3. Retrieve a record by email")
        print("4. Retrieve a record by phone number")
        print("5. Exit")

        choice = input("Please enter your choice: ")

        if choice == '1':
            insert_record()
        elif choice == '2':
            retrieve_by_id()
        elif choice == '3':
            retrieve_by_email()
        elif choice == '4':
            retrieve_by_phone()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the menu
menu()

# Close the connection to the database when done
connection.close()