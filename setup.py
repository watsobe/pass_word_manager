
################################################
# PASSWORD MANAGER ver 8.5
# setup.py
# Create and establish DB connectivity
# Benjamin Watson
###############################################

import sqlite3								# import SQL module to use commands

conn = sqlite3.connect('pwdatabase.db') 	# Create the DB and establish the connection
print(conn)									# Display connection information **ALERT

c = conn.cursor()							# establishing connection to execute SQL commands

# execution block used to create DB table with header names and values
c.execute("""CREATE TABLE passwords			
 	(id INTEGER PRIMARY KEY AUTOINCREMENT,	
 	website TEXT,
	username TEXT,
	password TEXT)""")

################################################
# TABLE CLEANUP SCRIPT
###############################################
#c.execute("DROP TABLE passwords")			# Fresh Start **CLEAR TABLE
#conn.commit()