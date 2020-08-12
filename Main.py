
################################################
# PASSWORD MANAGER ver 8.5
# main.py
# Execute Main Block of Code
# Benjamin Watson
###############################################

import sqlite3											# import SQL module to use commands
import os												# import operating system modules to use commands
import new_password										# import new_password.py object to use functions
import searchall										# import search_all.py object to use functions
import delete 											# import delete.py object to use functions

ADMIN_PASSWORD = "admin"								# Define local password
connect = input("Enter your password: ")				# Capture user input

while connect != ADMIN_PASSWORD:						# Verify correct pasword
	connect = input("Enter your password: ")
	if connect == 'q': break
	os.system('clear')


conn = sqlite3.connect('pwdatabase.db')					# Create the DB and establish the connection
c = conn.cursor()										# Establish connection to execute SQL commands
print(conn)												# Display connection information **ALERT


while True:												# Welcome Banner, Options Menu
	os.system('clear')
	print("\nWelcome to the Password Vault\n")
	print("Commands: ")
	print("s = See all passwords")
	print("n = New password")
	print("d = Delete password")
	print("q = Quit")
	print("\n")

	userInput = input("Enter a command: ")				# Capture user input
	
	if userInput == 's': searchall.search_all()			# Execution block - Calls function from imported modules based on user input
	elif userInput == 'n': new_password.new()
	elif userInput == 'd': delete.delete_password()
	elif userInput == 'q':
		break
